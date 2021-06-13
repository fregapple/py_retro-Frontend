import pygame, configparser
from pygame.locals import *



def frontend():
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

frontend()