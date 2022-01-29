import pygame, os
from collections import deque
from pathlib import Path
from .core_defaults import CoreDefaults
from .configmake import ConfigRead



# This is the pygame display class.
class Window():

    # Initial information to be loaded.
    def __init__(self):
        self.res = ConfigRead().DisplayRead()
        self.displayScreen = pygame.display.set_mode((self.res[0], self.res[1]))
        pygame.init()    
        self.display = 1
        self.clock = pygame.time.Clock()
        self.time_delta_stack = deque([])
        self.caption = pygame.display.set_caption("Py_Retro Frontend")
        
    # FIXME: (Seems the only function this now provides, it remembering the screen size for next launch.)
    # A call to resize all information of the pygame screen and write it to the config file.
    def resize(resolution_string):
        ConfigRead().DisplayWrite(resolution_string[0], resolution_string[1])
        # screenWidth = reso[0]
        # screenHeight = reso[1]

    # A call to refresh the information on the screen of the pygame window.
    def refresh(self):
        pygame.display.update()



# This brings in the last played game / so you don't have to search everytime you boot up.
class GameHistory():
    def __init__(self):
        self.__call__()

    def __call__(self):
        self.Ga, self.Co = ConfigRead().GameRead()


# This has all the images of the frontend loaded FIXME: and annoyingly it contains the Buttons.
class Images(pygame.sprite.Sprite):
    def __init__(self):
        self.__call__()
        pygame.sprite.Sprite.__init__(self)
        self.buttonF()
        self.__button__()
     
    # This loads the images and sets dimensions based on display resolution.
    def __call__(self):
        self.sizeget = Scale().size_get()
        self.scale = Scale().reso_scaler(self.sizeget[0], self.sizeget[1])
        self.bgM = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), (self.sizeget[0], self.sizeget[1]))
        self.bgR = pygame.transform.smoothscale(pygame.image.load('./examples/bgR2.jpg').convert(),(self.sizeget[0], self.sizeget[1]))
        self.bgS = pygame.transform.smoothscale(pygame.image.load('./examples/bgS.jpg').convert(),(self.sizeget[0], self.sizeget[1]))
        self.LRB = pygame.transform.smoothscale(pygame.image.load('./examples/LR2.jpg').convert(), (float(714.99*self.scale[0]), float(222.5*self.scale[1])))
        self.B2 = pygame.transform.smoothscale(pygame.image.load('./examples/B2.jpg').convert(), (float(711*self.scale[0]), float(220*self.scale[1])))
        self.B3 = pygame.transform.smoothscale(pygame.image.load('./examples/B3.jpg').convert(), (int(self.sizeget[0]/3.59), int(self.sizeget[1]/6.55)))
        self.Set = pygame.transform.smoothscale(pygame.image.load('./examples/S.jpg').convert(), (int(self.sizeget[0]/3.593), int(self.sizeget[1]/6.55)))
        self.Ex = pygame.transform.smoothscale(pygame.image.load('./examples/exit.jpg').convert(), (int(self.sizeget[0]/3.58), int(self.sizeget[1]/6.585)))
        self.Sg = pygame.transform.smoothscale(pygame.image.load('./examples/SG.jpg').convert(), (int(self.sizeget[0]/2.3107), int(self.sizeget[1]/10.55)))
        self.F1 = pygame.transform.smoothscale(pygame.image.load('./examples/f1.jpg').convert(), (int(self.sizeget[0]/12.925), int(self.sizeget[1]/10.45)))
        self.F2 = pygame.transform.smoothscale(pygame.image.load('./examples/f2.jpg').convert(), (int(self.sizeget[0]/12.85), int(self.sizeget[1]/10.5)))

    # This defines each button in the Frontend FIXME: Potentially swap to pygame_gui buttons
    def __button__(self):
        self.romM = Button(float(4*self.scale[0]),261*self.scale[1],float(714.99*self.scale[0]),float(221*self.scale[1]),colors.green, self.Rr)
        self.blank1 = Button(float(2.69999*self.scale[0]),float(484*self.scale[1]),float(711*self.scale[0]),float(220*self.scale[1]),colors.green, self.Bb1)
        self.blank2 = Button(self.sizeget[0]/float(600),self.sizeget[1]/float(2.019),float(self.sizeget[0]/3.61),float(self.sizeget[1]/7),colors.green,self.Bb2)
        self.setM = Button(self.sizeget[0]/float(800),self.sizeget[1]/float(1.54),float(self.sizeget[0]/3.61),float(self.sizeget[1]/7),colors.green, self.Ss)
        self.exit = Button(self.sizeget[0]/float(1000),self.sizeget[1]/float(1.252),float(self.sizeget[0]/3.58),float(self.sizeget[1]/6.585),colors.green,self.Ee)
        self.Start = Button(self.sizeget[0]/(2560/938),self.sizeget[1]/(2160/1470.5),int(self.sizeget[0]/2.3107),int(self.sizeget[1]/10.55),colors.green,self.Stt)
        self.loadR = Button(self.sizeget[0]/(2560/2078),self.sizeget[1]/(2160/795),int(self.sizeget[0]/12.925),int(self.sizeget[1]/10.45),colors.green,self.Ff1)
        self.loadC = Button(self.sizeget[0]/(2560/2073),self.sizeget[1]/(2160/1138),int(self.sizeget[0]/12.85),int(self.sizeget[1]/10.5),colors.green,self.Ff2)
        

    def buttonF(self):
        self.Rr = self.buttoncroper((714.99*self.scale[0], 222.5*self.scale[1]),self.LRB,120)
        self.Bb1 = self.buttoncroper((711*self.scale[0], 220*self.scale[1]), self.B2,120)
        self.Bb2 = self.buttoncroper((712*self.scale[0], 218*self.scale[1]), self.B3,120)
        self.Ss = self.buttoncroper((712.5*self.scale[0], 219.5*self.scale[1]), self.Set,100)
        self.Ee = self.buttoncroper((715*self.scale[0], 218.5*self.scale[1]), self.Ex,120)  
        self.Stt = self.buttoncroper((1107.889*self.scale[0], 136.49*self.scale[1]), self.Sg,170) 
        self.Ff1 = self.buttoncroper((198.065*self.scale[0], 137.799*self.scale[1]), self.F1,85)
        self.Ff2 = self.buttoncroper((199.221*self.scale[0], 137.142*self.scale[1]), self.F2,85) 

    def buttoncroper(self, surfaceSize, img, radius):
        self.original_image = pygame.Surface((surfaceSize))
        self.original_image.blit(img, (0, 0))
        self.image = self.original_image
        self.rect = self.image.get_rect()

        size = self.original_image.get_size()
        self.rect_image = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(self.rect_image, (255,255,200), (0, 0, *size), border_radius=int(radius*self.scale[0]))
        
        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)  

        return self.image
    # This call draws the buttons on the Frontend Main screen
    def frontend_buttons(self):
        x,y = pygame.mouse.get_pos()
        self.romM.draw(x,y)
        self.blank1.draw(x,y)
        self.blank2.draw(x,y)
        self.setM.draw(x,y)
        self.exit.draw(x,y)

    # This call draws the buttons on the Rom Menu screen
    def romMenu_buttons(self):
        x,y = pygame.mouse.get_pos()
        self.blank1.draw(x,y) 
        self.blank2.draw(x,y) 
        self.setM.draw(x,y)
        self.exit.draw(x,y) 
        self.loadR.draw(x,y)
        self.loadC.draw(x,y)
        self.Start.draw(x,y)

    # This call draws the buttons on the Settings Menu screen.
    def setMenu_buttons(self):
        x,y = pygame.mouse.get_pos()
        self.romM.draw(x,y)
        self.blank1.draw(x,y)
        self.blank2.draw(x,y)
        self.exit.draw(x,y)

    


# This class contains some basic colors.
class Colors():
    def __init__(self):
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.blue = (0,0,255)
        self.green = (0,255,0)
        self.purple = (255,0,255)
        self.yellow = (255,255,0)


# This class handles all the buttons and what they do.
class Button():
    
    def __init__(self, x, y, l, t, ac, imgon):
        self.x = x
        self.y = y
        self.l = l
        self.t = t
        self.ac = ac
        self.imgon = imgon
        self.zoom_scale = 1.05
        self.s = Scale().size_get()

    # This call provided a reaction to a click in the pygame.event process
    def action(self, click_x, click_y):
        self.Rect = pygame.Rect(self.x, self.y, self.l, self.t)
        if click_x > self.Rect.left and click_x < self.Rect.right and click_y > self.Rect.top and click_y < self.Rect.bottom:
            return True

    # This call draws the button to the window. Specifically it only draws it when the mouse is over the rect
    def draw(self, cursor_x, cursor_y):

        self.Rect = pygame.Rect(self.x, self.y, self.l, self.t)
        if cursor_x > self.Rect.left and cursor_x < self.Rect.right and cursor_y > self.Rect.top and cursor_y < self.Rect.bottom:
            self.s[2].blit(self.imgon, self.imgon.get_rect(center = self.Rect.center))

        else:
            pass


# This is the current text class.
class Text():
    pygame.font.init()

    def __init__(self, font, size, text, antialias, colour, background):
        self.sizeget = Scale().size_get()
        self.font = font
        self.size = size
        self.text = text
        self.antialias = antialias
        self.colour = colour
        self.background = background
        texts = pygame.font.SysFont(self.font, self.size, bold=True)
        self.text = texts.render(self.text, self.antialias, self.colour, self.background)

    # Annoyingly this needs to be doubled with the init. 
    def __call__(self, font, size, text, antialias, colour, background):
        self.sizeget = Scale().size_get()
        self.font = font
        self.size = size
        self.text = text
        self.antialias = antialias
        self.colour = colour
        self.background = background
        texts = pygame.font.SysFont(self.font, self.size, bold=True)
        self.text = texts.render(self.text, self.antialias, self.colour, self.background)

    # This call blits the text for the CORE
    def __coretext__(self):
        x, y = (self.sizeget[0]/1.71), (self.sizeget[1]/1.75)
        self.rect = self.text.get_rect(center=(x, y))
        self.sizeget[2].blit(self.text, self.rect)
        
    # This call blits the text for the ROM
    def __romtext__(self):
        x, y = float(self.sizeget[0]/1.71), float(self.sizeget[1]/2.4)
        self.rect = self.text.get_rect(center=(x, y))
        self.sizeget[2].blit(self.text, self.rect)
        
    
# This class defines each text object used. FIXME: can be implemented better, could maybe join into the above class.
class Texts():
    def __init__(self):
        self.__call__()

    def __call__(self):
        self.size = Scale().size_get()
        self.colors = Colors()
        self.gh = GameHistory()
        self.loadR = File().shorten_path(self.gh.Ga, 1)
        self.loadC = File().shorten_path(self.gh.Co, 1)
        self.text1 = Text('arial', int((self.size[0] + self.size[1])/90), f'{self.loadR}', True, self.colors.black, None)
        self.text2 = Text('arial', int((self.size[0] + self.size[1])/90), f'{self.loadC}', True, self.colors.black, None)


# This class is for each of the File Dialogs
class File():
    def __init__(self):
        self.CD = CoreDefaults
    # Call to select Core / writes said core to config file to be saved for next app opening
    def prompt2(self, lib_name):
        ConfigRead().GameWrite(lib_name, None, None)  
        
    # Call to select ROM / writes said ROM to config file to be saved for next app opening.
    # Also does a check to see if there is a default core and if there is will auto select it for simplicity
    def prompt1(self, file_name):
        file_extension = os.path.splitext(f'{file_name}')[1]
        ConfigRead().GameWrite(self.CD.coreCheck(file_extension), file_name, self.CD.coreCheck(file_extension))


    # Call to shorten path so text class can blit infomation that isn't a long thread. Can be used for other stuff.   
    def shorten_path(self, file_path, length):
        return Path(*Path(file_path).parts[-length:])

    # Call to write the Default cores. FIXME: not well implemented for cores that can do multiple ROMS EG .GB, .GBC
    def defaults(self, corename, option, manager, size):
        filename, file_extension = os.path.splitext(f'{corename}')
        file_name = str(self.shorten_path(filename, 1))
        if option == 1:
            self.CD.defaultChange(file_name, corename)
        elif option == 2:
            self.CD.specificCoreChange(file_name, corename, manager, size)

        

class Scale:
    def __init__(self):
        self.width = None
        self.height = None

    def size_get(self):
        self.s = pygame.display.get_surface()
        self.w, self.h = self.s.get_width(), self.s.get_height()
        return (self.w, self.h, self.s)

    def reso_scaler(self, sizeA, sizeB):
        self.width = (int(sizeA) / 2560)
        self.height = (int(sizeB) / 1440)
        return (self.width, self.height)
    
        
        

import pygame_gui, warnings
from pygame_gui.core.ui_element import UIElement
from pygame_gui.elements import UIWindow, UITextBox
from pygame_gui.elements import UIButton, UIDropDownMenu
from pygame_gui.elements import UIImage
from pygame_gui.windows import UIConfirmationDialog
from pygame_gui.core.interfaces import IUIManagerInterface
from pygame_gui._constants import UI_CONFIRMATION_DIALOG_CONFIRMED, UI_BUTTON_PRESSED, OldType
from pygame.event import custom_type
UI_CONFIRMATION_DIALOG_NO = custom_type()
UI_CONFIRMATION_DIALOG_YES = custom_type()
class PauseWindow(UIWindow):
    def __init__(self, rect, ui_manager):
        super().__init__(rect, ui_manager,
                          window_display_title='Paused',
                          resizable=False)

class DefaultSelector(UIWindow):
    def __init__(self, rect, ui_manager, item1, item2, item3, corename):
        super(). __init__(rect, ui_manager,
                            window_display_title='Default Change..',
                            resizable=False)
        current_item_string = f'{item1}'
        self.selector = UIDropDownMenu([f'{item1}',
                                        f'{item2}',
                                        f'{item3}'
                                        ],
                                        current_item_string,
                                        pygame.Rect((10, 10), (200,25)),
                                        ui_manager,
                                        container=self)
        

class ConfirmationDialogs(UIWindow):
    def __init__(self, rect: pygame.Rect,
                     manager:
                     IUIManagerInterface, 
                     action_long_desc: str, 
                     window_title: str = 'pygame-gui.Confirm',
                     action_short_name: str = 'pygame-gui.OK',
                     blocking: bool = False):
        super().__init__(rect, manager, window_display_title=window_title, resizable=False)
        
        minimum_dimensions = (260, 200)
        self.rect = rect
        self.manager = manager
        if rect.width < minimum_dimensions[0] or rect.height < minimum_dimensions[1]:
            warn_string = ("Initial size: " + str(rect.size) +
                           " is less than minimum dimensions: " + str(minimum_dimensions))
            warnings.warn(warn_string, UserWarning)
        self.set_minimum_dimensions(minimum_dimensions)

        self.cancel_button = UIButton(relative_rect=pygame.Rect(-10, -40, -1, 30),
                                      text='pygame-gui.Cancel',
                                      manager=self.ui_manager,
                                      container=self,
                                      object_id='#cancel_button',
                                      anchors={'left': 'right',
                                               'right': 'right',
                                               'top': 'bottom',
                                               'bottom': 'bottom'})

        self.no = UIButton(relative_rect=pygame.Rect(-10, -40, -1, 30),
                                       text=action_short_name,
                                       manager=self.ui_manager,
                                       container=self,
                                       object_id='#confirm_button',
                                       anchors={'left': 'right',
                                                'right': 'right',
                                                'top': 'bottom',
                                                'bottom': 'bottom',
                                                'left_target': self.cancel_button,
                                                'right_target': self.cancel_button})

        text_width = self.get_container().get_size()[0] - 10
        text_height = self.get_container().get_size()[1] - 50
        self.confirmation_text = UITextBox(html_text=action_long_desc,
                                           relative_rect=pygame.Rect(5, 5,
                                                                     text_width,
                                                                     text_height),
                                           manager=self.ui_manager,
                                           container=self,
                                           anchors={'left': 'left',
                                                    'right': 'right',
                                                    'top': 'top',
                                                    'bottom': 'bottom'})

        self.yes = UIButton(relative_rect=pygame.Rect(10, -40, -1, 30),
                                            text='Yes',
                                            manager=self.manager,
                                            container=self,
                                            anchors={'left': 'left',
                                                    'right': 'left',
                                                    'top': 'bottom',
                                                    'bottom': 'bottom'})

        self.set_blocking(blocking)



    def process_event(self, event: pygame.event.Event) -> bool:
        consumed_event = super().process_event(event)

        if event.type == UI_BUTTON_PRESSED and event.ui_element == self.cancel_button:
            self.kill()

        if event.type == UI_BUTTON_PRESSED and event.ui_element == self.no:
            # old event - to be removed in 0.8.0
            event_data = {'user_type': OldType(UI_CONFIRMATION_DIALOG_CONFIRMED),
                            'ui_element': self,
                            'ui_object_id': self.most_specific_combined_id}
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, event_data))
            # new event
            event_data = {'ui_element': self,
                            'ui_object_id': self.most_specific_combined_id}
            pygame.event.post(pygame.event.Event(UI_CONFIRMATION_DIALOG_NO, event_data))
            self.kill()
        
        if event.type == UI_BUTTON_PRESSED and event.ui_element == self.yes:
            event_data = {'ui_element': self,
                            'ui_object_id': self.most_specific_combined_id}
            pygame.event.post(pygame.event.Event(UI_CONFIRMATION_DIALOG_YES, event_data))
            self.kill()

        return consumed_event





            
colors = Colors()
        






        


        
        

