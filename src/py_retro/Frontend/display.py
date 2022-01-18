import pygame, os, configparser
from collections import deque
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE
from pathlib import Path
from .core_defaults import CoreDefaults

# For some reason needed to use this globally. FIXME: Can see if I can incorperate elsewhere
config = configparser.ConfigParser()
config.read("./py_retro/settings/config.txt")
DisplaySettings = config['Display Settings']
gameHistory = config['Last Opened Core / Game']
screenWidth = int(DisplaySettings['resolution width'])
screenHeight = int(DisplaySettings['resolution height'])
Ga = gameHistory['game']
Co = gameHistory['core']


# Think this is used for a below class to get resolution.
global displayScreen
displayScreen = pygame.display.set_mode((screenWidth, screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)
s = pygame.display.get_surface()
w, h = s.get_width(), s.get_height()


# This is the pygame display class.
class Window():

    # Initial information to be loaded.
    def __init__(self):

        self.displayScreen = pygame.display.set_mode((screenWidth, screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.res = (screenWidth, screenHeight)
        pygame.init()    
        self.display = 1
        self.clock = pygame.time.Clock()
        self.time_delta_stack = deque([])
        pygame.display.set_caption("Py_Retro Frontend")
        
    # A call to resize all information of the pygame screen and write it to the config file.
    def resize():
        global displayScreen
        s = pygame.display.get_surface()
        w = s.get_width() 
        h = s.get_height()
        config = configparser.ConfigParser()
        config.read("./py_retro/settings/config.txt")
        config.set('Display Settings', 'resolution width', f'{w}') 
        config.set('Display Settings', 'resolution height', f'{h}')   
        with open("./py_retro/settings/config.txt", "w") as configfile:
            config.write(configfile)
            config.read("./py_retro/settings/config.txt")
            DisplaySettings = config['Display Settings']
            screenWidth = int(DisplaySettings['resolution width'])
            screenHeight = int(DisplaySettings['resolution height'])
            displayScreen = pygame.display.set_mode((screenWidth, screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)
    
    # A call to refresh the information on the screen of the pygame window.
    def refresh(self):
        global screenWidth, screenHeight
        config.read("./py_retro/settings/config.txt")
        DisplaySettings = config['Display Settings']
        screenWidth = int(DisplaySettings['resolution width'])
        screenHeight = int(DisplaySettings['resolution height'])
        pygame.display.update()

    # Call to exit the window and end the Emulator.
    def exit(quit):
        pygame.quit()


# This brings in the last played game / so you don't have to search everytime you boot up.
class GameHistory():
    def __init__(self):
        self.__call__()

    def __call__(self):
        config.read("./py_retro/settings/config.txt")
        self.gh = config['Last Opened Core / Game']
        self.Ga = self.gh['game']
        self.Co = self.gh['core']


# This has all the images of the frontend loaded FIXME: and annoyingly it contains the Buttons.
class Images():
    def __init__(self):
        self.__call__()
        self.__button__()
    
    # This loads the images and sets dimensions based on display resolution.
    def __call__(self):
        self.s = pygame.display.get_surface()
        self.w, self.h = self.s.get_width(), self.s.get_height()
        self.config = configparser.ConfigParser()
        self.config.read("./py_retro/settings/config.txt")
        self.config.set('Display Settings', 'resolution width', f'{self.w}')
        self.config.set('Display Settings', 'resolution height', f'{self.h}')
        self.bgM = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), (self.w,self.h))
        self.bgR = pygame.transform.smoothscale(pygame.image.load('./examples/bgR2.jpg').convert(),(self.w,self.h))
        self.bgS = pygame.transform.smoothscale(pygame.image.load('./examples/bgS.jpg').convert(),(self.w,self.h))
        self.LRB = pygame.transform.smoothscale(pygame.image.load('./examples/LR2.jpg').convert(), (int(self.w/3.585), int(self.h/6.39)))
        self.B2 = pygame.transform.smoothscale(pygame.image.load('./examples/B2.jpg').convert(), (int(self.w/3.6), int(self.h/6.5)))
        self.B3 = pygame.transform.smoothscale(pygame.image.load('./examples/B3.jpg').convert(), (int(self.w/3.59), int(self.h/6.55)))
        self.Set = pygame.transform.smoothscale(pygame.image.load('./examples/S.jpg').convert(), (int(self.w/3.593), int(self.h/6.55)))
        self.Ex = pygame.transform.smoothscale(pygame.image.load('./examples/exit.jpg').convert(), (int(self.w/3.58), int(self.h/6.585)))
        self.Sg = pygame.transform.smoothscale(pygame.image.load('./examples/SG.jpg').convert(), (int(self.w/2.3107), int(self.h/10.55)))
        self.F1 = pygame.transform.smoothscale(pygame.image.load('./examples/f1.jpg').convert(), (int(self.w/12.925), int(self.h/10.45)))
        self.F2 = pygame.transform.smoothscale(pygame.image.load('./examples/f2.jpg').convert(), (int(self.w/12.85), int(self.h/10.5)))

    # This defines each button in the Frontend FIXME: Potentially swap to pygame_gui buttons
    def __button__(self):
        self.romM = Button(self.w/float(640),self.h/float(5.55),float(self.w/3.585),float(self.h/(6.39)),colors.green, self.LRB)
        self.blank1 = Button(self.w/float(948.14815),self.h/float(2.98),float(self.w/3.6),float(self.h/6.5),colors.green, self.B2)
        self.blank2 = Button(self.w/float(1163.636364),self.h/float(2.0175),float(self.w/3.61),float(self.h/7),colors.green,self.B3)
        self.setM = Button(self.w/float(1280),self.h/float(1.54),float(self.w/3.61),float(self.h/7),colors.green, self.Set)
        self.exit = Button(self.w/float(1280),self.h/float(1.252),float(self.w/3.58),float(self.h/6.585),colors.green,self.Ex)
        self.Start = Button(self.w/(2560/938),self.h/(2160/1470.5),int(self.w/2.3107),int(self.h/10.55),colors.green,self.Sg)
        self.loadR = Button(self.w/(2560/2078),self.h/(2160/795),int(self.w/12.925),int(self.h/10.45),colors.green,self.F1)
        self.loadC = Button(self.w/(2560/2073),self.h/(2160/1138),int(self.w/12.85),int(self.h/10.5),colors.green,self.F2)

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


# This class handles text objects. FIXME: I believe this has been superceded by a below class and not in use.
class TextObjects():
    
    def __init__(self,text,font):
        colors = Colors()
        self.textSurface = font.render(text, True, colors.white)
        return self.textSurface, self.textSurface.get_rect()


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

    # This call provided a reaction to a click in the pygame.event process
    def action(self, click_x, click_y):
        self.Rect = pygame.Rect(self.x, self.y, self.l, self.t)
        if click_x > self.Rect.left and click_x < self.Rect.right and click_y > self.Rect.top and click_y < self.Rect.bottom:
            return True

    # This call draws the button to the window. Specifically it only draws it when the mouse is over the rect
    def draw(self, cursor_x, cursor_y):
        self.Rect = pygame.Rect(self.x, self.y, self.l, self.t)
        if cursor_x > self.Rect.left and cursor_x < self.Rect.right and cursor_y > self.Rect.top and cursor_y < self.Rect.bottom:
            pygame.draw.rect(displayScreen, self.ac, self.Rect)
            displayScreen.blit(self.imgon, self.imgon.get_rect(center = self.Rect.center))

        else:
            pass


# This is the current text class.
class Text():
    pygame.font.init()

    def __init__(self, font, size, text, antialias, colour, background):
        self.s = pygame.display.get_surface()
        self.w, self.h = self.s.get_width(), self.s.get_height()
        self.config = configparser.ConfigParser()
        self.config.read("./py_retro/settings/config.txt")
        self.config.set('Display Settings', 'resolution width', f'{self.w}')
        self.config.set('Display Settings', 'resolution height', f'{self.h}')
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
        self.s = pygame.display.get_surface()
        self.w, self.h = self.s.get_width(), self.s.get_height()
        self.config = configparser.ConfigParser()
        self.config.read("./py_retro/settings/config.txt")
        self.config.set('Display Settings', 'resolution width', f'{self.w}')
        self.config.set('Display Settings', 'resolution height', f'{self.h}')
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
        x, y = (self.w/1.71), (self.h/1.75)
        self.rect = self.text.get_rect(center=(x, y))
        self.s.blit(self.text, self.rect)
        
    # This call blits the text for the ROM
    def __romtext__(self):
        x, y = float(self.w/1.71), float(self.h/2.4)
        self.rect = self.text.get_rect(center=(x, y))
        self.s.blit(self.text, self.rect)
        
    
# This class defines each text object used. FIXME: can be implemented better, could maybe join into the above class.
class Texts():
    def __init__(self):
        self.__call__()

    def __call__(self):
        global Ga, Co
        self.s = pygame.display.get_surface()
        self.w , self.h = self.s.get_width(), self.s.get_height()
        self.config = configparser.ConfigParser()
        self.config.read("./py_retro/settings/config.txt")
        self.config.set('Display Settings', 'resolution width', f'{self.w}')
        self.config.set('Display Settings', 'resoltuion height', f'{self.h}')
        self.colors = Colors()
        self.gh = GameHistory()
        self.loadR = File.shorten_path(self.gh.Ga, 1)
        self.loadC = File.shorten_path(self.gh.Co, 1)
        self.text1 = Text('arial', int((self.w + self.h)/90), f'{self.loadR}', True, self.colors.black, None)
        self.text2 = Text('arial', int((self.w + self.h)/90), f'{self.loadC}', True, self.colors.black, None)


# This class is for each of the File Dialogs
class File():
    
    # Call to select Core / writes said core to config file to be saved for next app opening
    def prompt2(lib_name):
        config.read("./py_retro/settings/config.txt")
        config.set('Last Opened Core / Game', 'core', f'{lib_name}')   
        with open("./py_retro/settings/config.txt", "w") as configfile:
            config.write(configfile)
            config.read("./py_retro/settings/config.txt")
        
        
    # Call to select ROM / writes said ROM to config file to be saved for next app opening.
    # Also does a check to see if there is a default core and if there is will auto select it for simplicity
    def prompt1(file_name):
        CD = CoreDefaults
        file_extension = os.path.splitext(f'{file_name}')[1]
        print(file_extension)
        config.read("./py_retro/settings/config.txt")
        config.set('Core Defaults', 'active core', f'{CD.coreCheck(file_extension)}')
        config.set('Last Opened Core / Game', 'core', f'{CD.coreCheck(file_extension)}')
        config.set('Last Opened Core / Game', 'game', f'{file_name}')   
        with open("./py_retro/settings/config.txt", "w") as configfile:
            config.write(configfile)
            config.read("./py_retro/settings/config.txt")

    # Call to shorten path so text class can blit infomation that isn't a long thread. Can be used for other stuff.   
    def shorten_path(file_path, length):
        return Path(*Path(file_path).parts[-length:])

    # Call to write the Default cores. FIXME: not well implemented for cores that can do multiple ROMS EG .GB, .GBC
    def Defaults(corename):
        CD = CoreDefaults
        filename, file_extension = os.path.splitext(f'{corename}')
        file_name = str(File.shorten_path(filename, 1))
        CD.defaultChange(file_name, corename)

# This is just a definer for above classes to use.
colors = Colors()        
        
        






        


        
        

