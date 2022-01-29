# TODO: Need to tidy the imports
import pygame, sys, os, pygame_gui
from pygame.locals import *
from pygame_gui import UIManager, PackageResource
from pygame_gui.core import ObjectID
from pygame_gui.windows import UIFileDialog, UIConfirmationDialog
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UILabel
from py_retro.core import EmulatedSystem

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py_retro.interactive import RetroEmu, RetroEmu2
from py_retro.Frontend import configmake
from py_retro.Frontend.main import *
from py_retro.Frontend.core_defaults import *
from py_retro.Frontend.display import *
from py_retro.Frontend.menu import *


# This finds the path for theme files. Helps when packaging with pyinstaller.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Emulator(UIWindow):
    def __init__(self, position, manager, libpath, rom):
        super().__init__(pygame.Rect(position, (1200, 900)), manager, 
                         window_display_title=f"{rom}")

        game_surface_size = self.get_container().get_size()
        self.game_surface_element = UIImage(pygame.Rect((0, 0), 
                                                         game_surface_size),
                                            pygame.Surface(game_surface_size).convert(),
                                            manager=manager,
                                            container=self,
                                            parent_element=self)

        self.emulator = RetroEmu(libpath)
        self.emulator.load_game(path=rom)
        self.is_active = True
        self.emulator.run()
        

    def process_event(self, event):
        handled = super().process_event(event)
        if (event.type == pygame_gui.UI_BUTTON_PRESSED and
                event.ui_element == self.title_bar):
            handled = True
            event_data = {'ui_element': self}
            
    # def update(self, time_delta):
    #     if self.alive() and self.is_active:
    #         self.emulator.update(time_delta)

    #     super().update(time_delta)

    #     self.emulator.draw(self.game_surface_element.image)


class Main:
    def __init__(self):
        # Sets the initial screensize for the GUI. Have a default theme added. Will need to create my own theme.
        self.manager = pygame_gui.UIManager((Window().res), resource_path('./data/themes/frontend_theme.json'))

        # Various class variables that get called
        self.screen = Window()
        self.screen2 = self.screen.displayScreen
        self.pics = Images()
        self.colors = Colors()
        self.texts = Texts()
        self.file = File()
        self.res = self.screen.res
        self.caption = self.screen.caption
        self.scale = Scale()

        # Here defines the UI Elements. They are NONE till the function recreate_gui defines them.
        self.resolution_drop = None
        

        # Menu Booleans. 
        self.RMenu = 0
        self.SMenu = 0
        self.FMenu = 0
        self.PMenu = 0
        self.counters = 0
        self.BD = False
        self.Game = False
        self.running = False
        self.file_dialog = None
        self.confirmation_dialog = None

        config = configparser.ConfigParser()
        config.read("./py_retro/settings/config.txt")
        gameHistory = config['Last Opened Core / Game']
        self.libpath = gameHistory['core']
        self.rompath = gameHistory['game']

        self.emulator_window_1 = None




    # GUI File Dialog that is now replacing TKinter.
    def open_file_dialog(self, choice):
        global file_dialog, prompt   
        self.s = pygame.display.get_surface()
        self.w, self.h = self.s.get_width(), self.s.get_height() 
        
        # FIXME: Want to be able to scale the window base on resolution. Also, to position it based on resolution.
        self.rect = pygame.Rect((0, 0), (450, 500))
        self.rect.center = self.screen2.get_rect().center

        #  There is possibly a better way of doing this, but this allows for multiple dialogs to do different things. 
        if choice == 1:       
            self.str = "Change Default Core"
            self.here = 'Libretro Cores/'
            self.prompt = 1
        if choice == 2:          
            self.str = "Picking Core"
            self.here = 'Libretro Cores/'
            self.prompt = 2
        if choice == 3:
            self.str = "Picking Rom"
            self.here = 'Games/'
            self.prompt = 3
        
        # This calls the Dialog Window to appear
        self.file_dialog = pygame_gui.windows.ui_file_dialog.UIFileDialog(rect=self.rect, 
                                                                          manager=self.manager,     
                                                                          window_title=self.str, 
                                                                          initial_file_path=self.here, 
                                                                          allow_picking_directories=False, 
                                                                          allow_existing_files_only=True)  

    def open_confirm_dialog(self, text):
        global confirmation_dialog, prompt2   
        self.rect=pygame.Rect(100,100, 350, 250)
        self.rect.center = self.screen2.get_rect().center                                                              
        self.confirmation_dialog = ConfirmationDialogs(self.rect, self.manager, 
            "Do you want to change ALL of the defaults relevant for this core? Press NO if you want to select the platform for the default.", 
                                                        action_short_name='No')
        return text

    """
                                                        MAIN LOOP
    """

    def Frontend(self): 
        self.FMenu = 1
        self.SMenu = 0
        self.RMenu = 0
        self.recreate_ui()        
        
        # While loop determines the state of the running cycle.
        while self.screen.display and self.FMenu == 1:

            # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
            #   however, too low caused the cursor to flicker too quick and not be able to open directories.
            time_delta = self.screen.clock.tick(120) / 1000.0
            self.screen.time_delta_stack.append(time_delta)

            # This allows a smoother frame rate for all pygame_GUI specific material.
            if len(self.screen.time_delta_stack) > 2000:
                self.screen.time_delta_stack.popleft()

            # All events are in a separate funciton at the bottom of this file. I wanted it on a different script, but 
            # cant get it to work.
            self.process_events()
            self.manager.update(time_delta)\

            # Blits the Background image. 
            self.screen.displayScreen.blit(self.pics.bgM, (0, 0)) 

            # These are the Menu buttons
            self.pics.frontend_buttons()

            # GUI specific calls
            self.manager.update(time_delta) 
            self.manager.draw_ui(self.screen2)
            
            # Refreshes the display to show the above.
            self.screen.refresh()

    """
                                                        ROM MENU LOOP
    """
    def RomMenu(self):

        # While loop determines the state of the running cycle.
        self.SMenu = 0
        self.FMenu = 0
        self.RMenu = 1
        self.recreate_ui()
        while self.screen.display and self.RMenu == 1:

            # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
            #   however, too low caused the cursor to flicker too quick and not be able to open directories.
            time_delta = self.screen.clock.tick(120) / 1000.0
            self.screen.time_delta_stack.append(time_delta)

            # This allows a smoother frame rate for all pygame_GUI specific material.
            if len(self.screen.time_delta_stack) > 2000:
                self.screen.time_delta_stack.popleft()

            # All events are in a separate funciton at the bottom of this file. I wanted it on a different script, but 
            # cant get it to work.
            self.process_events()
            self.manager.update(time_delta)

            # Blits the Background image.  
            self.screen.displayScreen.blit(self.pics.bgR, (0, 0)) 

            # Menu Buttons
            self.pics.romMenu_buttons()
            
            # Calls to populate the screen
            GameHistory().__call__()
            self.texts.__call__()
            self.texts.text1.__romtext__()
            self.texts.text2.__coretext__()

            # GUI specific calls
            self.manager.update(time_delta) 
            self.manager.draw_ui(self.screen2)

            # Refreshes the display to show the above.
            self.screen.refresh()

    """
                                                        SETTINGS MENU LOOP
    """
    def SetMenu(self):
        # While loop determines the state of the running cycle.
        self.SMenu = 1
        self.RMenu = 0
        self.FMenu = 0
        self.recreate_ui()
        while self.screen.display and self.SMenu == 1:

            # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
            #   however, too low caused the cursor to flicker too quick and not be able to open directories.
            time_delta = self.screen.clock.tick(120) / 1000.0
            self.screen.time_delta_stack.append(time_delta)

            # Drop Down goes here otherwise it is a black screen?
            
            # This allows a smoother frame rate for all pygame_GUI specific material.
            if len(self.screen.time_delta_stack) > 2000:
                self.screen.time_delta_stack.popleft()
                
            # All events are in a separate funciton at the bottom of this file. I wanted it on a different script, but 
            # cant get it to work.
            self.process_events()
            self.manager.update(time_delta)

            # Blits the Background image.
            self.screen.displayScreen.blit(self.pics.bgS, (0, 0)) 

            # Menu Buttons
            self.pics.setMenu_buttons()
        
            # GUI specific calls 
            self.manager.update(time_delta) 
            self.manager.draw_ui(self.screen2)

            # Updates the screen with the above content.
            self.screen.refresh()


    """
                                                        PAUSE MENU LOOP
    """
    # FIXME: I wonder if I can redo this pause menu completely. Perhaps run it all within pygame_gui, that partially 
    #           covers the screen and pauses the game in the background. Rather than looking exactly like the rest.

    def PauseMenu(self):
        self.rep = pygame.Rect((50, 50), ((self.res[0]*0.9), (self.res[1]*0.9)))
        self.rep.center = self.screen2.get_rect().center
        PauseWindow(self.rep, self.manager)
        
        # While loop determines the state of the running cycle.
        while self.screen.display and self.PMenu == 1:

            # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
            #   however, too low caused the cursor to flicker too quick and not be able to open directories.
            time_delta = self.screen.clock.tick(120) / 1000.0
            self.screen.time_delta_stack.append(time_delta)

            # This allows a smoother frame rate for all pygame_GUI specific material.
            if len(self.screen.time_delta_stack) > 2000:
                self.screen.time_delta_stack.popleft()
                
            # All events are in a separate funciton at the bottom of this file. I wanted it on a different script, but 
            # cant get it to work.
            self.process_events()
            self.manager.update(time_delta)


            # Blits the Background image.
            self.screen.displayScreen.blit(self.pics.bgS, (0, 0)) 

            # Menu Buttons
            self.pics.setMenu_buttons()

            # GUI specific calls 
            self.manager.update(time_delta) 
            self.manager.draw_ui(self.screen2)

            # Updates the screen with the above content.
            self.screen.refresh()


    """
                                    Emulator import based on Lifnings code: Complex Emulator
    """
    def main(self):

        # This loads the ROM and CORE based on what was written to the config file.
        config = configparser.ConfigParser()
        config.read("./py_retro/settings/config.txt")
        gameHistory = config['Last Opened Core / Game']
        self.libpath = gameHistory['core']
        self.rompath = gameHistory['game']
        self.newname = File().shorten_path(self.rompath, 1)
        pygame.display.set_caption(f"Py_Retro Frontend: {self.newname}")

        while self.Game is True:
            
            # This injects the CORE (libpath) into the various functions of lifnings code
            # Then loads the ROM (rompath)
            self.emu = RetroEmu(self.libpath)
            self.emu.load_game(path=self.rompath)
            self.running = True
            while self.running:
                self.emu.run()
                # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
                #   however, too low caused the cursor to flicker too quick and not be able to open directories.
                time_delta = self.screen.clock.tick() / 1000.0
                self.screen.time_delta_stack.append(time_delta)

                # This allows a smoother frame rate for all pygame_GUI specific material.
                if len(self.screen.time_delta_stack) > 2000:
                    self.screen.time_delta_stack.popleft()

                # All events are in a separate funciton at the bottom of this file. I wanted it on a different script, but 
                # cant get it to work.
                self.process_events()
                self.manager.update(time_delta)

 
                self.manager.draw_ui(self.screen2)
                self.screen.refresh()

    """
                                        Draws the GUI Elements
    """

    def recreate_ui(self):
        print(self.SMenu)
        self.manager.set_window_resolution(self.res)
        self.manager.clear_and_reset()
        current_resolution_string = (str(self.res[0]) +
                                     'x' +
                                     str(self.res[1]))
                           
        if self.SMenu == 1:
            self.scale.reso_scaler(self.res[0], self.res[1])                            
            self.resolution_drop = UIDropDownMenu(['640x480', '896x504', '800x600', '1152x648', '1024x768', 
                                                   '1280x720','1440x1080', '1920x1080', '1920x1440', '2560x1440'],
                                                    current_resolution_string,
                                                    pygame.Rect((int(self.res[0] / 2),
                                                                int(self.res[1] * 0.3)),
                                                                ((200*self.scale.width), int(25*self.scale.height))),
                                                    self.manager)                                   
        
    """
                                    Checks for Resolution changes
    """

    def check_resolution_changed(self):
        self.resolution_string = self.resolution_drop.selected_option.split('x')
        self.w2 = int(self.resolution_string[0])
        self.h2 = int(self.resolution_string[1])
        if (self.w2 != self.res[0] or self.h2 != self.res[1]):
            self.res = (self.w2, self.h2)
            pygame.display.set_mode(self.res)
            Window.resize(self.resolution_string)


    # This is a separate event handler. helps make the main file a bit more readable. Would love to be able shift this 
    #       to another script. probably not possible.
    def process_events(self):        
        
        # Pygame event handler. 
        for x in pygame.event.get():
            if x.type == QUIT:
                quit()


            self.manager.process_events(x)

            # Button Based Events
            if x.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = pygame.mouse.get_pos()
                mouse_buttons = pygame.mouse.get_pressed()

                # Button to go to the Rom Menu. also turns off menu specific values
                if self.pics.romM.action(click_x, click_y) and mouse_buttons[0] and self.BD == False:
                    self.manager.clear_and_reset()
                    self.RomMenu()
                
                # Button to go to the Settings Menu. Also turns off menu specific values.
                elif self.pics.setM.action(click_x, click_y) and mouse_buttons[0] and self.BD == False:
                    self.manager.clear_and_reset()
                    self.SetMenu()

                # Quits
                elif self.pics.exit.action(click_x, click_y) and mouse_buttons[0] and self.BD == False:
                    quit()
                # Opens Dialog for Core Default
                elif (self.pics.blank1.action(click_x, click_y) and self.FMenu == 1 
                            and mouse_buttons[0] and self.BD == False):
                    self.BD = True
                    self.manager.clear_and_reset()
                    self.open_file_dialog(1)
                
                elif (self.pics.blank2.action(click_x, click_y) and self.FMenu == 1
                            and mouse_buttons[0] and self.BD == False):
                    self.emulator_window_1 = Emulator((25,25), self.manager, self.libpath, self.rompath)

                elif (self.pics.blank2.action(click_x, click_y) and self.PMenu == 1 
                            and mouse_buttons[0] and self.BD == False):
                    try:
                        with open(f'{self.rompath}.state', 'rb') as f:
                            self.emu.unserialize(f.read())
                            print('loaded state.')
                    except IOError:
                        print('could not read state.')
                # Opens Dialog for selecting ROM 
                elif (self.pics.loadR.action(click_x, click_y) and self.RMenu == 1
                            and mouse_buttons[0] and self.BD == False):
                    self.BD = True
                    self.manager.clear_and_reset()
                    self.open_file_dialog(3)   
                # Opens Dialog for selecting CORE
                elif (self.pics.loadC.action(click_x, click_y) and self.RMenu == 1 
                            and mouse_buttons[0] and self.BD == False):
                    self.BD = True
                    self.manager.clear_and_reset()
                    self.open_file_dialog(2)
                # Starts the Emulator with the chosen files.
                # BUG: Need to setup a error message, rather than crashing when incorrect files are loaded and then 
                #       emulator has started.
                elif (self.pics.Start.action(click_x, click_y) and self.RMenu == 1 
                            and mouse_buttons[0] and self.BD == False):
                    self.Game = True
                    self.manager.clear_and_reset()
                    self.main()
                    

            # How escape moves through the menus
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_ESCAPE:
                    if self.Game == 1 and self.PMenu == 1:
                        self.PMenu = 0
                        self.FMenu = 0
                        self.SMenu = 0
                        self.RMenu = 0
                        self.BD = False
                        self.manager.clear_and_reset()
                    elif self.Game == 1 and self.PMenu == 0:
                        self.PMenu = 1
                        self.PauseMenu()
                    else:    
                        self.manager.clear_and_reset()
                        self.Frontend()

                    """FIXME: These 2/3 events are emulator specific. There will be more added in the future."""

                # Pressing F2 will save the state. State will be in the same location as the ROM file
                        # This one is only while a game is loaded within the system
                elif x.key == pygame.K_F2:
                    try:
                        with open(f'{self.rompath}.state', 'wb') as f:
                            f.write(self.emu.serialize())
                            print('saved state.')
                    except IOError:
                        print('could not write state.')

                # Pressing F4 will load the state. State will be in the same location as the ROM file
                        # This one is only while a game is loaded within the system
                elif x.key == pygame.K_F4:
                    try:
                        with open(f'{self.rompath}.state', 'rb') as f:
                            self.emu.unserialize(f.read())
                            print('loaded state.')
                    except IOError:
                        print('could not read state.')
                elif x.key == K_l:
                    self.PMenu = 1
                    self.BD = True
                    self.PauseMenu()
                    
                # Pressing m will close the game if needed.
                elif x.key == pygame.K_m:
                    quit() 
                    
            # Once an option is selected from the Dialog, the path is directed to the respective function.
            if x.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                if x.ui_element == self.file_dialog and self.prompt == 1:
                    self.hey = self.open_confirm_dialog(x.text)
    
                    
                elif x.ui_element == self.file_dialog and self.prompt == 2:
                    File().prompt2(x.text)
                    
                elif x.ui_element == self.file_dialog and self.prompt == 3:
                    File().prompt1(x.text)


            # This handles what happens when you close a GUI window. Relevant for Disabled buttons as if you close a file
                    # dialog without choosing a file, buttons would still be disabled.
            if x.type == pygame_gui.UI_WINDOW_CLOSE:
                if x.ui_element == self.file_dialog:
                    self.BD = False
            
            if x.type == pygame_gui.UI_WINDOW_CLOSE and PauseWindow:
                if self.Game == 1 and self.PMenu == 1 and self.BD == True:
                    self.FMenu = 0
                    self.SMenu = 0
                    self.RMenu = 0
                    self.BD = False
                    self.manager.clear_and_reset()

            # This is the new Resolution Handler. I didn't want to use the VIDEORESIZE any more. This will stop people
                    # Making irregular sizings. Whilst it scales fine, it is just simpler to have set resolutions.
                        # FIXME: I'd like to incorporate a load screen whilst the screen rescales the images.
            if x.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if x.ui_element == self.resolution_drop:
                    self.check_resolution_changed()
                    self.pics.__call__()
                    self.pics.buttonF() 
                    self.pics.__button__()
                    self.texts.__call__()
                    GameHistory().__call__()
                    self.texts.text1.__romtext__()
                    self.texts.text2.__coretext__() 
                    self.manager.set_window_resolution(self.res)  
                    self.recreate_ui()  
                           
                    self.screen.refresh()

            if x.type == UI_CONFIRMATION_DIALOG_YES:
                if x.ui_element == self.confirmation_dialog:
                    File().defaults(self.hey, 1, None, None)

            if x.type == UI_CONFIRMATION_DIALOG_NO:
                if x.ui_element == self.confirmation_dialog:
                    s = Scale().size_get()
                    File().defaults(self.hey, 2, self.manager, (s[0],s[1],s[2]))
            

Main().Frontend()