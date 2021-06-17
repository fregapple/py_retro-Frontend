import pygame, sys, os, configparser, tkinter.filedialog
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE

config = configparser.ConfigParser()
config.read("./py_retro/settings/config.txt")
DisplaySettings = config['Display Settings']
screenWidth = int(DisplaySettings['resolution width'])
screenHeight = int(DisplaySettings['resolution height'])
displayScreen = pygame.display.set_mode((screenWidth, screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)
s = pygame.display.get_surface()
w, h = s.get_width(), s.get_height()


class Window():
    def __init__(self):

        self.displayScreen = pygame.display.set_mode((screenWidth, screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.res = (screenWidth, screenHeight)
        pygame.init()
    
        self.display = 1
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("py_retro Frontend")

    def resize(self, config, w, h):
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
            config.read("../settings/config.txt")
            DisplaySettings = config['Display Settings']
            screenWidth = int(DisplaySettings['resolution width'])
            screenHeight = int(DisplaySettings['resolution height'])
            displayScreen = pygame.display.set_mode((screenWidth, screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)
            pygame.display.flip()  

    def tick(self,fps):
        self.clock.tick(fps)
    
    def refresh(self):
        pygame.display.flip()

    def exit():
        quit()

        
        


class Images():
    def __init__(self):
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




class Colors():
    def __init__(self):
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.blue = (0,0,255)
        self.green = (0,255,0)
        self.purple = (255,0,255)
        self.yellow = (255,255,0)

class TextObjects():
    
    def __init__(self,text,font):
        colors = Colors()
        self.textSurface = font.render(text, True, colors.white)
        return self.textSurface, self.textSurface.get_rect()

class Button():
    def __init__(self,x, y, l, t, ic, ac, img, imgon, action=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.rect = pygame.Rect(x, y, l, t)
        on_button = self.rect.collidepoint(self.mouse)
        if on_button:
            pygame.draw.rect(displayScreen, ac, self.rect)
            displayScreen.blit(imgon, imgon.get_rect(center = self.rect.center))
        else:
            None
            # pygame.draw.rect(displayScreen, ic, self.rect)
            # displayScreen.blit(img, img.get_rect(center = self.rect.center))

        if on_button:
            if self.click[0] == 1 and action != None:
                action()


class File():
    def prompt1():
        top = tkinter.Tk()
        top.withdraw()
        lib_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()

        

