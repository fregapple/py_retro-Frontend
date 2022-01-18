# TODO: Need to tidy the imports
import pygame, sys, os, pygame_gui
from pygame.locals import *
from pygame_gui import UIManager, PackageResource

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py_retro.interactive import RetroEmu
from py_retro.Frontend import configmake
from py_retro.Frontend.main import *
from py_retro.Frontend.core_defaults import *
from py_retro.Frontend.display import *
from py_retro.Frontend.menu import *


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# TODO: Not sure if necessary.
global RMenu, SMenu

# Sets the initial screensize for the GUI. Have a default theme added. Will need to create my own theme.
manager = pygame_gui.UIManager((Window().res))

# Various class variables that get called
screen = Window()
screen2 = screen.displayScreen
pics = Images()
colors = Colors()
texts = Texts()
file = File()


# Menu Booleans. 
RMenu = False
SMenu = False

# mouse Position for buttons. TODO: Might not be needed as is in the loops
click_x, click_y = pygame.mouse.get_pos()

# GUI File Dialog that is now replacing TKinter.
# FIXME: need to disable clickthrough / need to change theme coloring
def open_file_dialog(choice):
    global file_dialog, prompt    

    rect = pygame.Rect((0,0), (600, 400))
    rect.center = screen2.get_rect().center

    #  There is possibly a better way of doing this, but this allows for multiple dialogs to do different things. 
    if choice == 1:     
        prompt = 1   
    if choice == 2:          
        prompt = 2
    if choice == 3:
        prompt = 3

    # This calls the Dialog Window to appear
    file_dialog = pygame_gui.windows.ui_file_dialog.UIFileDialog(rect=rect, manager=manager, allow_picking_directories=False)

                                                
                                                
"""
                                                    MAIN LOOP
"""

def Frontend():   
    
    # While loop determines the state of the running cycle.
    while screen.display == 1:

        # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
        #   however, too low caused the cursor to flicker too quick and not be able to open directories.
        time_delta = screen.clock.tick() / 1000.0
        screen.time_delta_stack.append(time_delta)

        # This allows a smoother frame rate for all pygame_GUI specific material.
        if len(screen.time_delta_stack) > 2000:
            screen.time_delta_stack.popleft()

        # Pygame event handler. 
        for x in pygame.event.get():
            if x.type == QUIT:
                screen.exit()
            
            # Button Based Events
            elif x.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = pygame.mouse.get_pos()

                if pics.romM.action(click_x, click_y):
                    RomMenu()
                elif pics.setM.action(click_x, click_y):
                    SetMenu()
                elif pics.exit.action(click_x, click_y):
                    screen.exit()
                elif pics.blank1.action(click_x, click_y):
                    open_file_dialog(1)
                    
            # Once an option is selected from the Dialog, the path is directed to the respective function.
            if x.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                if x.ui_element == file_dialog and prompt == 1:
                    File.Defaults(x.text)

            # Rescales all the content on screen. 
            elif x.type == VIDEORESIZE:
                pygame.display.set_mode(x.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                Window.resize()
                pics.__call__()
                pics.__button__()
                manager.set_window_resolution(x.size)
                screen.refresh()
            
            # Updates pygame_gui specific events      
            manager.process_events(x)
        

        # Blits the Background image. 
        screen.displayScreen.blit(pics.bgM, (0, 0)) 

        # These are the Menu buttons
        pics.frontend_buttons()

        # GUI specific calls
        manager.update(time_delta) 
        manager.draw_ui(screen2) 
        
        # Refreshes the display to show the above.
        screen.refresh()

"""
                                                      ROM MENU LOOP
"""
def RomMenu():

    # While loop determines the state of the running cycle.
    RMenu = 1
    while screen.display and RMenu == 1:

        # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
        #   however, too low caused the cursor to flicker too quick and not be able to open directories.
        time_delta = screen.clock.tick() / 1000.0
        screen.time_delta_stack.append(time_delta)

        # This allows a smoother frame rate for all pygame_GUI specific material.
        if len(screen.time_delta_stack) > 2000:
            screen.time_delta_stack.popleft()

        # Start of Event Manager
        # TODO: Would like to have all events handled elsewhere with "manager.process_events(x)"
        for x in pygame.event.get():
            if x.type == QUIT:
                screen.display = 0
                screen.exit()

            # TODO: This is a great example of why moving this into it's own "manager.process_events(x) would be great."
            elif x.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = pygame.mouse.get_pos()

                # Moves to Settings Menu
                if pics.setM.action(click_x, click_y):
                    SetMenu()

                # Exits Frontend
                if pics.exit.action(click_x, click_y):
                    screen.exit()

                # Opens Dialog for selecting ROM 
                if pics.loadR.action(click_x, click_y):
                    open_file_dialog(3)
                
                # Opens Dialog for selecting CORE
                if pics.loadC.action(click_x, click_y):
                    open_file_dialog(2)

                # Starts the Emulator with the chosen files.
                # BUG: Need to setup a error message, rather than crashing when incorrect files are loaded and then 
                #           emulator has started.
                if pics.Start.action(click_x, click_y):
                    Main()

            # Once an option is selected from the Dialog, the path is directed to the respective function.
            if x.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                if x.ui_element == file_dialog and prompt == 2:
                    File.prompt2(x.text)
                elif x.ui_element == file_dialog and prompt == 3:
                    File.prompt1(x.text)

            # This allows you to go back through the menu to the previous page.
            elif x.type == pygame.KEYDOWN:
                        if x.key == pygame.K_ESCAPE:
                            RMenu = 0
                            Frontend()

            # Rescales all the content on screen. 
            elif x.type == VIDEORESIZE:
                pygame.display.set_mode(x.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                Window.resize()
                pics.__call__()
                pics.__button__()
                texts.__call__()
                GameHistory().__call__()
                texts.text1.__romtext__()
                texts.text2.__coretext__()
                manager.set_window_resolution(x.size)               
                screen.refresh()

            # This will hopefully be a place I can do the events else where, rather than each loop.
            manager.process_events(x)

        # Blits the Background image.  
        screen.displayScreen.blit(pics.bgR, (0, 0)) 

        # Menu Buttons
        pics.romMenu_buttons()
        
        # Calls to populate the screen
        GameHistory().__call__()
        texts.__call__()
        texts.text1.__romtext__()
        texts.text2.__coretext__()

        # GUI specific calls
        manager.update(time_delta) 
        manager.draw_ui(screen2)

        # Refreshes the display to show the above.
        screen.refresh()

"""
                                                      SETTINGS MENU LOOP
"""
def SetMenu():

    # While loop determines the state of the running cycle.
    SMenu = 1
    while screen.display and SMenu == 1:

        # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
        #   however, too low caused the cursor to flicker too quick and not be able to open directories.
        time_delta = screen.clock.tick() / 1000.0
        screen.time_delta_stack.append(time_delta)

        # This allows a smoother frame rate for all pygame_GUI specific material.
        if len(screen.time_delta_stack) > 2000:
            screen.time_delta_stack.popleft()
            
        for event in pygame.event.get():
            if event.type == QUIT:
                screen.display = 0
                screen.exit()

            # FIXME: This is a great example of why moving this into it's own "manager.process_events(x) would be great."
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = pygame.mouse.get_pos()

                if pics.romM.action(click_x, click_y):
                    RomMenu()
                if pics.exit.action(click_x, click_y):
                    screen.exit()

            # This allows you to go back through the menu to the previous page.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SMenu = 0
                    Frontend()
                    
            # Rescales all the content on screen. 
            elif event.type == VIDEORESIZE:
                pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                Window.resize() 
                pics.__call__()
                pics.__button__()
                manager.set_window_resolution(event.size)
                screen.refresh()
            
            # This will hopefully be a place I can do the events else where, rather than each loop.
            manager.process_events(event)

        # Blits the Background image.
        screen.displayScreen.blit(pics.bgS, (0, 0)) 

        # Menu Buttons
        pics.setMenu_buttons()

        # GUI specific calls 
        manager.update(time_delta) 
        manager.draw_ui(screen2)

        # Updates the screen with the above content.
        screen.refresh()


"""
                                                      PAUSE MENU LOOP
"""
def PauseMenu():

    # While loop determines the state of the running cycle.
    PMenu = 1
    while screen.display and PMenu == 1:

        # This need to be within the while loop to function correctly. Adjusting the clock.tick can speed up scrolling
        #   however, too low caused the cursor to flicker too quick and not be able to open directories.
        time_delta = screen.clock.tick() / 1000.0
        screen.time_delta_stack.append(time_delta)

        # This allows a smoother frame rate for all pygame_GUI specific material.
        if len(screen.time_delta_stack) > 2000:
            screen.time_delta_stack.popleft()
            
        for event in pygame.event.get():
            if event.type == QUIT:
                screen.display = 0
                screen.exit()

            # FIXME: This is a great example of why moving this into it's own "manager.process_events(x) would be great."
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = pygame.mouse.get_pos()

                if pics.romM.action(click_x, click_y):
                    RomMenu()
                if pics.exit.action(click_x, click_y):
                    screen.exit()

            # This allows you to go back through the menu to the previous page.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    PMenu = 0
                    
            # Rescales all the content on screen. 
            elif event.type == VIDEORESIZE:
                pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                Window.resize() 
                pics.__call__()
                pics.__button__()
                manager.set_window_resolution(event.size)
                screen.refresh()
            
            # This will hopefully be a place I can do the events else where, rather than each loop.
            manager.process_events(event)

        # Blits the Background image.
        screen.displayScreen.blit(pics.bgS, (0, 0)) 

        # Menu Buttons
        pics.setMenu_buttons()

        # GUI specific calls 
        manager.update(time_delta) 
        manager.draw_ui(screen2)

        # Updates the screen with the above content.
        screen.refresh()


"""
                                Emulator import based on Lifnings code: Complex Emulator
"""
def Main():
    global libpath, rompath, emu, Game, running

    # This loads the ROM and CORE based on what was written to the config file.
    config = configparser.ConfigParser()
    config.read("./py_retro/settings/config.txt")
    gameHistory = config['Last Opened Core / Game']
    libpath = gameHistory['core']
    rompath = gameHistory['game']
    Game = True

    while Game is True:
        
        # This injects the CORE (libpath) into the various functions of lifnings code
        # Then loads the ROM (rompath)
        emu = RetroEmu(libpath)
        emu.load_game(path=rompath)
        running = True
        while running:
            emu.run()
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    running = False
                    quit()

                if x.type == VIDEORESIZE:
                    pygame.display.set_mode(x.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                    Window.resize() 
                    pics.__call__()
                    texts.__call__()
                    GameHistory().__call__()
                    texts.text1.__romtext__()
                    texts.text2.__coretext__()
                    screen.refresh()
                    
                elif x.type == pygame.KEYDOWN:
                    if x.key == pygame.K_ESCAPE:
                        # running = False
                        # Game = False
                        PauseMenu()
                        
                    
                    # Pressing F2 will save the state. State will be in the same location as the ROM file
                    if x.key == pygame.K_F2:
                        try:
                            with open(f'{rompath}.state', 'wb') as f:
                                f.write(emu.serialize())
                                print('saved state.')
                        except IOError:
                            print('could not write state.')

                    # Pressing F4 will load the state. State will be in the same location as the ROM file
                    elif x.key == pygame.K_F4:
                        try:
                            with open(f'{rompath}.state', 'rb') as f:
                                emu.unserialize(f.read())
                                print('loaded state.')
                        except IOError:
                            print('could not read state.')

                    # This records gameplay. Possibly broken, haven't tried with my implementation.
                    elif x.key == pygame.K_o:
                        try:
                            with emu.til_record(open(f'{rompath}.til', 'wb')):
                                print('recording til, press ESC to end...')
                                while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
                                    emu.run()
                                    pygame.event.pump()
                                print('done recording til.')
                        except IOError:
                            print('could not write til.')

                    # This plays back the recorded gameplay.
                    elif x.key == pygame.K_p:
                        try:
                            with emu.til_playback(open(f'{rompath}.til', 'rb')):
                                print('playing til, press ESC to cancel...')
                                while emu.til_is_playing() and not pygame.key.get_pressed()[pygame.K_ESCAPE]:
                                    emu.run()
                                    pygame.event.pump()
                                print('done playing til.')
                        except IOError:
                            print('could not read til.')

                    # Pressing m will close the game if needed.
                    elif x.key == pygame.K_m:
                        quit() 
Frontend()