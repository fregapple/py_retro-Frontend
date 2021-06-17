import pygame, ctypes, sys, os, tkinter, tkinter.filedialog, time, configparser

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py_retro.Frontend import *
from py_retro.Frontend.display import *
from pygame.locals import *
screen = Window()
pics = Images()
colors = Colors()

RMenu = False
SMenu = False
def Frontend():

    while screen.display == 1:

        mainMenu = True
        while mainMenu == True:

            for x in pygame.event.get():
                if x.type == QUIT:
                    screen.display = 0
                    screen.exit()
                
                if x.type == VIDEORESIZE:
                    # global displayScreen
                    pygame.display.set_mode(x.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                    Window.resize(w, h, config, displayScreen) 
                    pics.__call__()
                    screen.refresh()

            screen.tick(60)
            screen.displayScreen.blit(pics.bgM, (0, 0)) 

            Button(pics.w/(2560/4),pics.h/5.55,int(pics.w/3.585),int(pics.h/6.39),colors.red,colors.green,None,pics.LRB, RomMenu)
            Button(pics.w/(2560/2.7),pics.h/2.98,int(pics.w/3.6),int(pics.h/6.5),colors.red,colors.green,None,pics.B2, None) 
            Button(pics.w/(2560/2.2),pics.h/2.0175,int(pics.w/3.61),int(pics.h/7),colors.red,colors.green,None,pics.B3, None) 
            Button(pics.w/(2560/2),pics.h/1.54,int(pics.w/3.61),int(pics.h/7),colors.red,colors.green,None,pics.Set,SetMenu)
            Button(pics.w/(2560/2),pics.h/1.252,int(pics.w/3.58),int(pics.h/6.585),colors.red,colors.green,None,pics.Ex, screen.exit)                      # These are the Menu Buttons
            screen.refresh() 


        screen.refresh()

def RomMenu():

    RMenu = True
    while RMenu == True:
        for x in pygame.event.get():
            if x.type == QUIT:
                screen.display = 0
                screen.exit()

            if x.type == VIDEORESIZE:
                pygame.display.set_mode(x.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                Window.resize(w, h, config, displayScreen) 
                pics.__call__()
                screen.refresh()

        screen.tick(60)
        screen.displayScreen.blit(pics.bgR, (0, 0)) 

        Button(pics.w/(2560/2.7),pics.h/2.98,int(pics.w/3.6),int(pics.h/6.5),colors.red,colors.green,None,pics.B2, None) 
        Button(pics.w/(2560/2.2),pics.h/2.0175,int(pics.w/3.61),int(pics.h/7),colors.red,colors.green,None,pics.B3, None) 
        Button(pics.w/(2560/2),pics.h/1.54,int(pics.w/3.61),int(pics.h/7),colors.red,colors.green,None,pics.Set,SetMenu)
        Button(pics.w/(2560/2),pics.h/1.252,int(pics.w/3.58),int(pics.h/6.585),colors.red,colors.green,None,pics.Ex, screen.exit) 
        Button(pics.w/(2560/2078),pics.h/(2160/795),int(pics.w/12.925),int(pics.h/10.45),colors.red,colors.green,None,pics.F1, File.prompt1) 
        Button(pics.w/(2560/2073),pics.h/(2160/1138),int(pics.w/12.85),int(pics.h/10.5),colors.red,colors.green,None,pics.F2, None) 
        Button(pics.w/(2560/938),pics.h/(2160/1470.5),int(pics.w/2.3107),int(pics.h/10.55),colors.red,colors.green,None,pics.Sg, None) 
        screen.refresh()

def SetMenu():
   
    SMenu = True
    while SMenu == True:
        for x in pygame.event.get():
            if x.type == QUIT:
                screen.display = 0
                screen.exit()

            if x.type == VIDEORESIZE:
                # global displayScreen
                pygame.display.set_mode(x.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                Window.resize(w, h, config, displayScreen) 
                pics.__call__()
                screen.refresh()

        screen.tick(60)
        screen.displayScreen.blit(pics.bgS, (0, 0)) 

        Button(pics.w/(2560/4),pics.h/5.55,int(pics.w/3.585),int(pics.h/6.39),colors.red,colors.green,None,pics.LRB, RomMenu)
        Button(pics.w/(2560/2.7),pics.h/2.98,int(pics.w/3.6),int(pics.h/6.5),colors.red,colors.green,None,pics.B2, None) 
        Button(pics.w/(2560/2.2),pics.h/2.0175,int(pics.w/3.61),int(pics.h/7),colors.red,colors.green,None,pics.B3, None) 
        Button(pics.w/(2560/2),pics.h/1.252,int(pics.w/3.58),int(pics.h/6.585),colors.red,colors.green,None,pics.Ex, screen.exit) 
        # Button(pics.w/3,pics.h/3,int(pics.w/3.61),int(pics.h/7),colors.red,colors.green,None,pics.B3,None)
        screen.refresh()
Frontend()