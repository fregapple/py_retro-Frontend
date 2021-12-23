import pygame, configparser
from pygame.locals import *
# from Frontend2 import *
# from py_retro.Frontend.main import *

# class Images():
#     def __init__(self):
#         self.__call__()

#     def __call__(self):
#         self.s = pygame.display.get_surface()
#         self.w, self.h = self.s.get_width(), self.s.get_height()
#         self.config = configparser.ConfigParser()
#         self.config.read("../settings/config.txt")
#         self.config.set('Display Settings', 'resolution width', f'{self.w}')
#         self.config.set('Display Settings', 'resolution height', f'{self.h}')
#         self.bgM = pygame.transform.smoothscale(pygame.image.load('../../examples/bg2.jpg').convert(), (self.w,self.h))
#         self.bgR = pygame.transform.smoothscale(pygame.image.load('../../examples/bgR2.jpg').convert(),(self.w,self.h))
#         self.bgS = pygame.transform.smoothscale(pygame.image.load('../../examples/bgS.jpg').convert(),(self.w,self.h))
#         self.LRB = pygame.transform.smoothscale(pygame.image.load('../../examples/LR2.jpg').convert(), (int(self.w/3.585), int(self.h/6.39)))
#         self.B2 = pygame.transform.smoothscale(pygame.image.load('../../examples/B2.jpg').convert(), (int(self.w/3.6), int(self.h/6.5)))
#         self.B3 = pygame.transform.smoothscale(pygame.image.load('../../examples/B3.jpg').convert(), (int(self.w/3.59), int(self.h/6.55)))
#         self.Set = pygame.transform.smoothscale(pygame.image.load('../../examples/S.jpg').convert(), (int(self.w/3.593), int(self.h/6.55)))
#         self.Ex = pygame.transform.smoothscale(pygame.image.load('../../examples/exit.jpg').convert(), (int(self.w/3.58), int(self.h/6.585)))
#         self.Sg = pygame.transform.smoothscale(pygame.image.load('../../examples/SG.jpg').convert(), (int(self.w/2.3107), int(self.h/10.55)))
#         self.F1 = pygame.transform.smoothscale(pygame.image.load('../../examples/f1.jpg').convert(), (int(self.w/12.925), int(self.h/10.45)))
#         self.F2 = pygame.transform.smoothscale(pygame.image.load('../../examples/f2.jpg').convert(), (int(self.w/12.85), int(self.h/10.5)))



def mainMenu():
    pygame.init()

    # Resolution from settings file
    res = configparser.ConfigParser()
    res.read("../settings/config.txt")
    d = res['Display Settings']
    screenW = int(d['resolution width'])
    screenH = int(d['resolution height'])
    reso = (screenW, screenH)
    display = pygame.display.set_mode(reso, HWSURFACE|DOUBLEBUF|RESIZABLE)
    pygame.display.set_caption("Test")
    

    # Background
    bg = pygame.transform.smoothscale(pygame.image.load(r"../../examples/bg2.jpg").convert(), reso)
    clock = pygame.time.Clock()

    display.blit(bg, (0, 0))
    pygame.display.update()

    running = True
    while running is True:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == VIDEORESIZE:
                display = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                reso = event.size
                bg = pygame.transform.smoothscale(pygame.image.load(r"../../examples/bg2.jpg").convert(), reso)
                display.blit(bg, (0, 0))
                

        pygame.display.flip()

