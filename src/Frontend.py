
import pygame, ctypes, sys, os, tkinter, tkinter.filedialog, pathlib, time, configparser

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pygame.locals import *
from py_retro.Frontend import configmake
#from pathlib import Path
from subprocess import SubprocessError
#from py_retro.recording import AVRecorderSystem
from py_retro.tas import TilRecorderInputMixin, TilPlayerInputMixin
from py_retro.interactive import PygameSystem
#from py_retro.core import EmulatedSystem

class FeaturedSystem(
    TilRecorderInputMixin,
    TilPlayerInputMixin,
    #AVRecorderSystem,
    PygameSystem
):
    pass


# Global Conditions
running = False
gameExit = False
settings = False
mainEmu = False
mainMenu = False
coreMenu = False
romMenu = False
sett = False
resol1 = False
resol2 = False
resol3 = False
resol4 = False
pause = False
ressettings = False
changedSettings = False
file_name = "Load Rom"
lib_name = "Load Cores"

config = configparser.ConfigParser()
config.read("./py_retro/settings/config.txt")
DisplaySettings = config['Display Settings']
screenWidth = int(DisplaySettings['resolution width'])
screenHeight = int(DisplaySettings['resolution height'])
displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
res = (screenWidth, screenHeight)
bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)
# lr = pygame.transform.smoothscale(pygame.image.load('./examples/LR.jpg').convert_alpha())




def frontend():

    global settings, mainEmu, running
    mainEmu = False
    running = False

        
    pygame.init()

    # VARIABLES

    # Screen Size and Window information

    #print(screenWidth, screenHeight)
    displayScreen = pygame.display.set_mode((screenWidth, screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)    # Sets screen size
    pygame.display.set_caption("My Frontend")                               # Titles the window
    #icon = pygame.image.load()
    #pygame.display.set_icon(icon)                                          # Loads the above image as the window and task bar icon.
    clock = pygame.time.Clock()                                           # Framerate

    # Colours
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    blue = (0,0,255)
    green = (0,255,0)
    purple = (255,0,255)
    yellow = (255,255,0)
    backgrFill = (100,255,100)


    # Background
    #background = pygame.image.load()

    # Game Definitions

        

    def close():

        pygame.quit()
        quit()

    
    def message_display(text):

        largeText = pygame.font.Font('comicsansms',115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((screenWidth/2),(screenHeight/2))
        displayScreen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

    def text_objects(text, font):

        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()

    def button2(x, y, l, t, ic, ac, img, imgon, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        rect = pygame.Rect(x, y, l, t)
        on_button = rect.collidepoint(mouse)
        if on_button:
            pygame.draw.rect(displayScreen, ac, rect)
            displayScreen.blit(imgon, imgon.get_rect(center = rect.center))
        else:
            None
            # pygame.draw.rect(displayScreen, ic, rect)
            # displayScreen.blit(img, img.get_rect(center = rect.center))

        if on_button:
            if click[0] == 1 and action != None:
                action()



    def button(msg,a,b,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)


        if a+w > mouse[0] > a and b+h > mouse[1] > b:
            pygame.draw.rect(displayScreen, ac,(a,b,w,h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(displayScreen, ic,(a,b,w,h))
            
        smallText = pygame.font.SysFont("comicsansms",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (a+(w/2)), (b+(h/2)) )
        displayScreen.blit(textSurf, textRect)

    def menuMain():
        global mainMenu, mainEmu, bg1, displayScreen, screenWidth, screenHeight, w, h
        s = pygame.display.get_surface()
        w, h = s.get_width(), s.get_height()
        imageOn = pygame.transform.smoothscale(pygame.image.load('./examples/LR2.jpg').convert(), (int(w/3.585), int(h/6.39)))
        imageOn2 = pygame.transform.smoothscale(pygame.image.load('./examples/B2.jpg').convert(), (int(w/3.6), int(h/6.5)))
        imageOn3 = pygame.transform.smoothscale(pygame.image.load('./examples/B3.jpg').convert(), (int(w/3.59), int(h/6.55)))
        imageOn4 = pygame.transform.smoothscale(pygame.image.load('./examples/S.jpg').convert(), (int(w/3.593), int(h/6.55)))
        imageOn5 = pygame.transform.smoothscale(pygame.image.load('./examples/exit.jpg').convert(), (int(w/3.58), int(h/6.585)))   

        while mainMenu is True:
            # s = pygame.display.get_surface()
            # w, h = s.get_width(), s.get_height()
            for event in pygame.event.get():

                if event.type  == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        frontend()

                if event.type == VIDEORESIZE:
                    pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                    s = pygame.display.get_surface()
                    w, h = s.get_width(), s.get_height()
                    config = configparser.ConfigParser()
                    test = displayScreen.copy()
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
                    bg1 = pygame.transform.smoothscale(pygame.image.load(r'./examples/bg2.jpg').convert(),(w,h))
                    imageOn = pygame.transform.smoothscale(pygame.image.load('./examples/LR2.jpg').convert(), (int(w/3.585), int(h/6.39)))
                    imageOn2 = pygame.transform.smoothscale(pygame.image.load('./examples/B2.jpg').convert(), (int(w/3.6), int(h/6.5)))
                    imageOn3 = pygame.transform.smoothscale(pygame.image.load('./examples/B3.jpg').convert(), (int(w/3.59), int(h/6.55)))
                    imageOn4 = pygame.transform.smoothscale(pygame.image.load('./examples/S.jpg').convert(), (int(w/3.593), int(h/6.55)))
                    imageOn5 = pygame.transform.smoothscale(pygame.image.load('./examples/exit.jpg').convert(), (int(w/3.58), int(h/6.585)))

                    pygame.display.flip()

            if mainEmu is True:
                global lib_name, file_name
                libpath = lib_name
                emu = FeaturedSystem(libpath)
                emu.unload()
                emu.__del__()
                mainEmu = False
                #menuMain()



            # Displayed Background of Main Menu
            
            #displayScreen.fill(blue)
            clock.tick(165)
            displayScreen.blit(bg1, (0, 0))                       # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen
             
            button2(w/(2560/4),h/5.55,int(w/3.585),int(h/6.39),red,green,None,imageOn, menuRom)
            button2(w/(2560/2.7),h/2.98,int(w/3.6),int(h/6.5),red,green,None,imageOn2, None) 
            button2(w/(2560/2.2),h/2.0175,int(w/3.61),int(h/7),red,green,None,imageOn3, None) 
            button2(w/(2560/2),h/1.54,int(w/3.61),int(h/7),red,green,None,imageOn4, menuSettings)
            button2(w/(2560/2),h/1.252,int(w/3.58),int(h/6.585),red,green,None,imageOn5, close)                      # These are the Menu Buttons

            # Screen refresh and update section
            
            pygame.display.flip()


    def menuRom():
        global mainMenu, mainEmu, bg1, displayScreen, screenWidth, screenHeight, w, h, lib_name, file_name
        bg1 = pygame.transform.smoothscale(pygame.image.load(r'./examples/bgR.jpg').convert(),(w,h))
        s = pygame.display.get_surface()
        w, h = s.get_width(), s.get_height()
        imageOn2 = pygame.transform.smoothscale(pygame.image.load('./examples/B2.jpg').convert(), (int(w/3.6), int(h/6.5)))
        imageOn3 = pygame.transform.smoothscale(pygame.image.load('./examples/B3.jpg').convert(), (int(w/3.59), int(h/6.55)))
        imageOn4 = pygame.transform.smoothscale(pygame.image.load('./examples/S.jpg').convert(), (int(w/3.593), int(h/6.55)))
        imageOn5 = pygame.transform.smoothscale(pygame.image.load('./examples/exit.jpg').convert(), (int(w/3.58), int(h/6.585)))   

        while mainMenu is True:

            for event in pygame.event.get():

                if event.type  == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        frontend()

                if event.type == VIDEORESIZE:
                    pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                    s = pygame.display.get_surface()
                    w, h = s.get_width(), s.get_height()
                    config = configparser.ConfigParser()
                    test = displayScreen.copy()
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
                    bg1 = pygame.transform.smoothscale(pygame.image.load(r'./examples/bgR.jpg').convert(),(w,h))
                    imageOn2 = pygame.transform.smoothscale(pygame.image.load('./examples/B2.jpg').convert(), (int(w/3.6), int(h/6.5)))
                    imageOn3 = pygame.transform.smoothscale(pygame.image.load('./examples/B3.jpg').convert(), (int(w/3.59), int(h/6.55)))
                    imageOn4 = pygame.transform.smoothscale(pygame.image.load('./examples/S.jpg').convert(), (int(w/3.593), int(h/6.55)))
                    imageOn5 = pygame.transform.smoothscale(pygame.image.load('./examples/exit.jpg').convert(), (int(w/3.58), int(h/6.585)))

                    pygame.display.flip()
                if mainEmu is True:
                    libpath = lib_name
                    emu = FeaturedSystem(libpath)
                    emu.unload()
                    emu.__del__()
                    mainEmu = False
                    #menuMain()



            # Displayed Background of Main Menu
            
            #displayScreen.fill(blue)
            clock.tick(165)
            displayScreen.blit(bg1, (0, 0))                       # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen
             
            # button2(w/(2560/4),h/5.55,int(w/3.585),int(h/6.39),red,green,image,imageOn, menuRom)
            button2(w/(2560/2.7),h/2.98,int(w/3.6),int(h/6.5),red,green,None,imageOn2, None) 
            button2(w/(2560/2.2),h/2.0175,int(w/3.61),int(h/7),red,green,None,imageOn3, None) 
            button2(w/(2560/2),h/1.54,int(w/3.61),int(h/7),red,green,None,imageOn4, menuSettings)
            button2(w/(2560/2),h/1.252,int(w/3.58),int(h/6.585),red,green,None,imageOn5, close)
            button(file_name,screenWidth/3,screenHeight-200,screenWidth/2,50,red,green,prompt_file)                    
            button(lib_name,screenWidth/3,screenHeight-140,screenWidth/2,50,red,green,prompt_file2)
            button("Start Game",screenWidth/3,screenHeight-80,screenWidth/2,50,red,green,main)   
          # These are the Menu Buttons

            # Screen refresh and update section
            
            pygame.display.flip()

        # global mainMenu
        # global romMenu
        # global file_name
        # global lib_name
        # mainMenu = False
        # romMenu = True

        # while romMenu is True:

        #     for event in pygame.event.get():



        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()

        #         if event.type == pygame.KEYDOWN:

        #             if event.key == pygame.K_ESCAPE:
        #                 romMenu = False
        #                 mainMenu = True
                        



        #     # Displayed Background of Main Menu
        #     displayScreen.fill(purple)
        #     #displayScreen.fill(background (0, 0))                          # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

        #     # What is Displayed on the Screen

        #     largeText = pygame.font.SysFont("comicsansms",40)               # This is Title Text
        #     TextSurf, TextRect = text_objects("System Roms", largeText)
        #     TextRect.center = ((screenWidth/2),(screenHeight/2))
        #     displayScreen.blit(TextSurf, TextRect)



        #     # button(file_name,5,screenHeight-200,screenWidth-10,50,red,green,prompt_file)                    # These are the Menu Buttons
        #     # button(lib_name,5,screenHeight-140,screenWidth-10,50,red,green,prompt_file2)
        #     # button("Start Game",5,screenHeight-80,screenWidth-10,50,red,green,main)

        #     # Screen refresh and update section
        #     clock.tick(60)
        #     pygame.display.update()

    def menuSettings():
        global mainMenu, mainEmu, bg1, displayScreen, screenWidth, screenHeight, w, h, lib_name, file_name
        bg1 = pygame.transform.smoothscale(pygame.image.load(r'./examples/bgS.jpg').convert(),(w,h))
        s = pygame.display.get_surface()
        w, h = s.get_width(), s.get_height()
        image = pygame.transform.smoothscale(pygame.image.load('./examples/LR.jpg').convert(), (int(w/3.585), int(h/6.39))) 
        imageOn = pygame.transform.smoothscale(pygame.image.load('./examples/LR2.jpg').convert(), (int(w/3.585), int(h/6.39)))
        imageOn2 = pygame.transform.smoothscale(pygame.image.load('./examples/B2.jpg').convert(), (int(w/3.6), int(h/6.5)))
        imageOn3 = pygame.transform.smoothscale(pygame.image.load('./examples/B3.jpg').convert(), (int(w/3.59), int(h/6.55)))
        imageOn5 = pygame.transform.smoothscale(pygame.image.load('./examples/exit.jpg').convert(), (int(w/3.58), int(h/6.585)))   

        while mainMenu is True:

            for event in pygame.event.get():

                if event.type  == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        frontend()

                if event.type == VIDEORESIZE:
                    pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                    s = pygame.display.get_surface()
                    w, h = s.get_width(), s.get_height()
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
                    bg1 = pygame.transform.smoothscale(pygame.image.load(r'./examples/bgS.jpg').convert(),(w,h))
                    image = pygame.transform.smoothscale(pygame.image.load('./examples/LR.jpg').convert(), (int(w/3.585), int(h/6.39))) 
                    imageOn = pygame.transform.smoothscale(pygame.image.load('./examples/LR2.jpg').convert(), (int(w/3.585), int(h/6.39)))
                    imageOn2 = pygame.transform.smoothscale(pygame.image.load('./examples/B2.jpg').convert(), (int(w/3.6), int(h/6.5)))
                    imageOn3 = pygame.transform.smoothscale(pygame.image.load('./examples/B3.jpg').convert(), (int(w/3.59), int(h/6.55)))
                    imageOn5 = pygame.transform.smoothscale(pygame.image.load('./examples/exit.jpg').convert(), (int(w/3.58), int(h/6.585)))

                    pygame.display.flip()
                if mainEmu is True:
                    libpath = lib_name
                    emu = FeaturedSystem(libpath)
                    emu.unload()
                    emu.__del__()
                    mainEmu = False
                    #menuMain()



            # Displayed Background of Main Menu
            
            #displayScreen.fill(blue)
            clock.tick(165)
            displayScreen.blit(bg1, (0, 0))                       # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen
             
            button2(w/(2560/4),h/5.55,int(w/3.585),int(h/6.39),red,green,image,imageOn, menuRom)
            button2(w/(2560/2.7),h/2.98,int(w/3.6),int(h/6.5),red,green,image,imageOn2, None) 
            button2(w/(2560/2.2),h/2.0175,int(w/3.61),int(h/7),red,green,image,imageOn3, None) 
            button2(w/(2560/2),h/1.252,int(w/3.58),int(h/6.585),red,green,image,imageOn5, close)  
            button("800x600",screenWidth/3,screenHeight-200,screenWidth/2,50,red,green,reso1)            # These are the Menu Buttons
            button("Fullscreen",screenWidth/3,screenHeight-140,screenWidth/2,50,red,green,reso4)
            button("1440x1080",screenWidth/3,screenHeight-80,screenWidth/2,50,red,green,reso3)
            
                   
            # Screen refresh and update section
            
            pygame.display.flip()
        # global mainMenu
        # global settingsMenu
        # mainMenu = False
        # settingsMenu = True

        # while settingsMenu is True:

        #     for event in pygame.event.get():

        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()

        #         if event.type == pygame.KEYDOWN:

        #             if event.key == pygame.K_ESCAPE:
        #                 settingsMenu = False
        #                 mainMenu = True

        #     # Displayed Background of Main Menu
        #     displayScreen.fill(yellow)
        #     #displayScreen.fill(background (0, 0))                          # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

        #     # What is Displayed on the Screen

        #     largeText = pygame.font.SysFont("comicsansms",40)               # This is Title Text
        #     TextSurf, TextRect = text_objects("Settings!", largeText)
        #     TextRect.center = ((screenWidth/2),(screenHeight/2))
        #     displayScreen.blit(TextSurf, TextRect)

        #     button("800x600",5,screenHeight-200,screenWidth-10,50,red,green,reso1)            # These are the Menu Buttons
        #     button("Fullscreen",5,screenHeight-140,screenWidth-10,50,red,green,reso4)
        #     button("1440x1080",5,screenHeight-80,screenWidth-10,50,red,green,reso3)
            

        #     # Screen refresh and update section
        #     clock.tick(60)
        #     pygame.display.update()

    def prompt_file():
        global file_name


        top = tkinter.Tk()
        top.withdraw()
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        

    def prompt_file2():
        global lib_name

        top = tkinter.Tk()
        top.withdraw()
        lib_name = tkinter.filedialog.askopenfilename(parent=top)
        print(lib_name)
        top.destroy()
        

    def paused(): 
        global pause

        while pause is True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        pause = False
                        

            # Displayed Background of Main Menu
            displayScreen.fill(blue)
            #displayScreen.fill(background (0, 0))                          # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen

            largeText = pygame.font.SysFont("comicsansms",40)               # This is Title Text
            TextSurf, TextRect = text_objects("Paused Menu!", largeText)
            TextRect.center = ((screenWidth/2),(screenHeight/6))
            displayScreen.blit(TextSurf, TextRect)

            button("Close Rom",screenWidth/3,screenHeight/3,screenWidth/3,50,red,green,romexit)                    # These are the Menu Buttons
            button("Roms",screenWidth/3,screenHeight/3+75,screenWidth/3,50,red,green,menuRom)
            button("Settings",screenWidth/3,screenHeight/3+150,screenWidth/3,50,red,green,menuSettings)
            button("Quit",screenWidth/3,screenHeight/3+225,screenWidth/3,50,red,green,close)

            # Screen refresh and update section
            clock.tick(165)
            pygame.display.update() 

    def reso1():
        global screenWidth, screenHeight, resol1, displayScreen, pause, bg1, res, w, h
        resol1 = True
        while resol1 is True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if pause == False and event.key == pygame.K_RETURN:
                        resol1 = False
                        config = configparser.ConfigParser()
                        config.read("./py_retro/settings/config.txt")
                        config.set('Display Settings', 'resolution width', '800')
                        config.set('Display Settings', 'resolution height', '600')

                        with open("./py_retro/settings/config.txt", "w") as configfile:
                            config.write(configfile)
                            config.read("../settings/config.txt")
                            DisplaySettings = config['Display Settings']
                            screenWidth = int(DisplaySettings['resolution width'])
                            screenHeight = int(DisplaySettings['resolution height'])
                            displayScreen = pygame.display.set_mode((screenWidth, screenHeight))                            
                        displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        res = (screenWidth, screenHeight)
                        s = pygame.display.get_surface()
                        w, h = s.get_width(), s.get_height()
                        bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)

                    if pause == True and event.key == pygame.K_RETURN:
                        config = configparser.ConfigParser()
                        config.read("./py_retro/settings/config.txt")
                        config.set('Display Settings', 'resolution width', '800')
                        config.set('Display Settings', 'resolution height', '600')

                        with open("./py_retro/settings/config.txt", "w") as configfile:
                            config.write(configfile)
                            config.read("./py_retro/settings/config.txt")
                            DisplaySettings = config['Display Settings']
                            screenWidth = int(DisplaySettings['resolution width'])
                            screenHeight = int(DisplaySettings['resolution height'])
                            displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        res = (screenWidth, screenHeight)
                        bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)
                        resol1 = False
                        return
            # Displayed Background of Main Menu
            displayScreen.fill(yellow)
            #displayScreen.fill(background (0, 0))                          # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen

            largeText = pygame.font.SysFont("comicsansms",40)               # This is Title Text
            TextSurf, TextRect = text_objects("Are you Sure? Press enter for Yes", largeText)
            TextRect.center = ((screenWidth/2),(screenHeight/2))
            displayScreen.blit(TextSurf, TextRect)
            clock.tick(165)
            pygame.display.flip()

    def reso2():
        global screenWidth, screenHeight, resol2, displayScreen, pause, bg1
        resol2 = True

        while resol2 is True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if pause == False and event.key == pygame.K_RETURN:
                        resol2 = False
                        config = configparser.ConfigParser()
                        config.read("./py_retro/settings/config.txt")
                        config.set('Display Settings', 'resolution width', '1024')
                        config.set('Display Settings', 'resolution height', '768')

                        with open("./py_retro/settings/config.txt", "w") as configfile:
                            config.write(configfile)
                            config.read("./py_retro/settings/config.txt")
                            DisplaySettings = config['Display Settings']
                            screenWidth = int(DisplaySettings['resolution width'])
                            screenHeight = int(DisplaySettings['resolution height'])
                            displayScreen = pygame.display.set_mode((screenWidth, screenHeight))                            
                        displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        res = (screenWidth, screenHeight)
                        bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)

                    if pause == True and event.key == pygame.K_RETURN:
                        config = configparser.ConfigParser()
                        config.read("./py_retro/settings/config.txt")
                        config.set('Display Settings', 'resolution width', '1024')
                        config.set('Display Settings', 'resolution height', '768')
                        
                        with open("./py_retro/settings/config.txt", "w") as configfile:
                            config.write(configfile)
                            config.read("./py_retro/settings/config.txt")
                            DisplaySettings = config['Display Settings']
                            screenWidth = int(DisplaySettings['resolution width'])
                            screenHeight = int(DisplaySettings['resolution height'])
                            displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        res = (screenWidth, screenHeight)
                        bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)
                        resol2 = False
                        return    

            # Displayed Background of Main Menu
            displayScreen.fill(yellow)
            #displayScreen.fill(background (0, 0))                          # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen

            largeText = pygame.font.SysFont("comicsansms",40)               # This is Title Text
            TextSurf, TextRect = text_objects("Are you Sure? Press enter for Yes", largeText)
            TextRect.center = ((screenWidth/2),(screenHeight/2))
            displayScreen.blit(TextSurf, TextRect)
            clock.tick(165)
            pygame.display.update()

    def reso3():
        global screenWidth, screenHeight, resol3, displayScreen, pause, bg1
        resol3 = True

        while resol3 is True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if pause == False and event.key == pygame.K_RETURN:
                        #screenWidth, screenHeight = res1
                        resol3 = False
                        config = configparser.ConfigParser()
                        config.read("./py_retro/settings/config.txt")
                        config.set('Display Settings', 'resolution width', '1440')
                        config.set('Display Settings', 'resolution height', '1080')

                        with open("./py_retro/settings/config.txt", "w") as configfile:
                            config.write(configfile)
                            config.read("./py_retro/settings/config.txt")
                            DisplaySettings = config['Display Settings']
                            screenWidth = int(DisplaySettings['resolution width'])
                            screenHeight = int(DisplaySettings['resolution height'])
                            displayScreen = pygame.display.set_mode((screenWidth, screenHeight))                            
                        displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        res = (screenWidth, screenHeight)
                        bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)

                    if pause == True and event.key == pygame.K_RETURN:
                        config = configparser.ConfigParser()
                        config.read("./py_retro/settings/config.txt")
                        config.set('Display Settings', 'resolution width', '1440')
                        config.set('Display Settings', 'resolution height', '1080')
                        
                        with open("./py_retro/settings/config.txt", "w") as configfile:
                            config.write(configfile)
                            config.read("./py_retro/settings/config.txt")
                            DisplaySettings = config['Display Settings']
                            screenWidth = int(DisplaySettings['resolution width'])
                            screenHeight = int(DisplaySettings['resolution height'])
                            displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        res = (screenWidth, screenHeight)
                        bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)
                        resol3 = False
                        return

            # Displayed Background of Main Menu
            displayScreen.fill(yellow)
            #displayScreen.fill(background (0, 0))                          # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen

            largeText = pygame.font.SysFont("comicsansms",40)               
            TextSurf, TextRect = text_objects("Are you Sure? Press enter for Yes", largeText) # This is Title Text
            TextRect.center = ((screenWidth/2),(screenHeight/2))
            displayScreen.blit(TextSurf, TextRect)
            clock.tick(165)
            pygame.display.update()

    def reso4():
        global screenWidth, screenHeight, resol4, displayScreen, pause, bg1
        resol4 = True

        while resol4 is True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if pause == False and event.key == pygame.K_RETURN:
                        #screenWidth, screenHeight = res1
                        resol4 = False
                        config = configparser.ConfigParser()
                        config.read("./py_retro/settings/config.txt")
                        config.set('Display Settings', 'resolution width', '0')
                        config.set('Display Settings', 'resolution height', '0')

                        with open("./py_retro/settings/config.txt", "w") as configfile:
                            config.write(configfile)
                            config.read("./py_retro/settings/config.txt")
                            DisplaySettings = config['Display Settings']
                            screenWidth = int(DisplaySettings['resolution width'])
                            screenHeight = int(DisplaySettings['resolution height'])
                            displayScreen = pygame.display.set_mode((screenWidth, screenHeight))                            
                        displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        res = (screenWidth, screenHeight)
                        bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)

                    if pause == True and event.key == pygame.K_RETURN:
                        config = configparser.ConfigParser()
                        config.read("./py_retro/settings/config.txt")
                        config.set('Display Settings', 'resolution width', '0')
                        config.set('Display Settings', 'resolution height', '0')
                        
                        with open("./py_retro/settings/config.txt", "w") as configfile:
                            config.write(configfile)
                            config.read("./py_retro/settings/config.txt")
                            DisplaySettings = config['Display Settings']
                            screenWidth = int(DisplaySettings['resolution width'])
                            screenHeight = int(DisplaySettings['resolution height'])
                            displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
                        res = (0, 0)
                        bg1 = pygame.transform.smoothscale(pygame.image.load('./examples/bg2.jpg').convert(), res)
                        resol4 = False
                        return

            # Displayed Background of Main Menu
            displayScreen.fill(yellow)
            #displayScreen.fill(background (0, 0))                          # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen

            largeText = pygame.font.SysFont("comicsansms",40)               
            TextSurf, TextRect = text_objects("Are you Sure? Press enter for Yes", largeText) # This is Title Text
            TextRect.center = ((screenWidth/2),(screenHeight/2))
            displayScreen.blit(TextSurf, TextRect)
            clock.tick(165)
            pygame.display.flip()

    def ressettings():
        global menuSettings
        ressettings = True
        while ressettings is True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        ressettings = False
                        menuSettings = False

            # Displayed Background of Main Menu
            displayScreen.fill(yellow)
            #displayScreen.fill(background (0, 0))                          # This whole section of Backgrounds can be removed if I chose to stick with Main Loop Background.

            # What is Displayed on the Screen

            largeText = pygame.font.SysFont("comicsansms",40)               # This is Title Text
            TextSurf, TextRect = text_objects("Settings!", largeText)
            TextRect.center = ((screenWidth/2),(screenHeight/2))
            displayScreen.blit(TextSurf, TextRect)

            button("800x600",5,screenHeight-200,screenWidth-10,50,red,green,reso1)            # These are the Menu Buttons
            button("1024x768",5,screenHeight-140,screenWidth-10,50,red,green,reso2)
            button("1440x1080",5,screenHeight-80,screenWidth-10,50,red,green,reso3)
            

            # Screen refresh and update section
            clock.tick(165)
            pygame.display.update()    

    def romexit():
        global running, mainMenu, lib_name
        libpath = lib_name
        running = False
        mainMenu = True
        emu = FeaturedSystem(libpath)
        emu.unload()
        emu.__del__()
        menuMain()
 

    def main():
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        global pause, mainEmu, lib_name, file_name, running, mainMenu, running
        libpath = lib_name
        rompath = file_name
        mainEmu = True
        fullscreen = False

        while mainEmu is True:

            emu = FeaturedSystem(libpath)
            emu.load_game(path=rompath)

            # TODO: it'd be cool to support doing these simultaneously, like...
            # - recording a TIL from a subset of another TIL
            # - rendering a TIL to video
            # - making a savestate in the middle of a TIL
            # - adding checkpoint savestates while recording a TIL
            running = True
            while running:
                emu.run()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pause = True
                            paused()
                        if event.key == pygame.K_F2:
                            try:
                                with open(f'{rompath}.state', 'wb') as f:
                                    f.write(emu.serialize())
                                    print('saved state.')
                            except IOError:
                                print('could not write state.')
                        elif event.key == pygame.K_F4:
                            try:
                                with open(f'{rompath}.state', 'rb') as f:
                                    emu.unserialize(f.read())
                                    print('loaded state.')
                            except IOError:
                                print('could not read state.')
                        elif event.key == pygame.K_o:
                            try:
                                with emu.til_record(open(f'{rompath}.til', 'wb')):
                                    print('recording til, press ESC to end...')
                                    while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
                                        emu.run()
                                        pygame.event.pump()
                                    print('done recording til.')
                            except IOError:
                                print('could not write til.')
                        elif event.key == pygame.K_p:
                            try:
                                with emu.til_playback(open(f'{rompath}.til', 'rb')):
                                    print('playing til, press ESC to cancel...')
                                    while emu.til_is_playing() and not pygame.key.get_pressed()[pygame.K_ESCAPE]:
                                        emu.run()
                                        pygame.event.pump()
                                    print('done playing til.')
                            except IOError:
                                print('could not read til.')
                        elif event.key == pygame.K_v:
                            try:
                                with emu.av_record(f'{rompath}.webm', ['-c:v', 'libvpx-vp9']):
                                    print('recording video, press ESC to end...')
                                    while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
                                        emu.run()
                                        pygame.event.pump()
                                    print('done recording video.')
                            except SubprocessError:
                                print('could not invoke ffmpeg.')
                        elif event.key == pygame.K_m:
                            romexit()
                            # running = False
                            # mainMenu = True
                            # emu.unload()
                            # emu.__del__()
                            # menuMain()
                        if fullscreen is False:
                            if pygame.key.get_pressed()[pygame.K_LALT] and pygame.key.get_pressed()[pygame.K_RETURN]:
                                fullscreen = True
                                pygame.display.set_mode((screenWidth, screenHeight))
                                pygame.display.flip()
                            else:
                                None
                                
                            
                                
                        if fullscreen is True:
                            if pygame.key.get_pressed()[pygame.K_LALT] and pygame.key.get_pressed()[pygame.K_RETURN]:
                                fullscreen = False
                                pygame.display.set_mode((screenWidth, screenHeight))
                                pygame.display.flip()
                            else:
                                None
                                
                            # #emu.__del__()


                            
                            


        if __name__ == "__main__":
            main()


    # Frontend Loop

    while not gameExit:

        for event in pygame.event.get():

            if event.type  == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    global mainMenu
                    mainMenu = True
                    menuMain()


        # Displayed Background
        displayScreen.fill(backgrFill)
        #displayScreen.fill(background (0, 0))                              # Uncomment this if there is a background selected in Variables
        largeText = pygame.font.SysFont("comicsansms",40)
        TextSurf, TextRect = text_objects("Press Enter!", largeText)
        TextRect.center = ((screenWidth/2),(screenHeight/2))
        displayScreen.blit(TextSurf, TextRect)

        # Screen refresh and update section
        clock.tick(165)
        pygame.display.update()
frontend()





