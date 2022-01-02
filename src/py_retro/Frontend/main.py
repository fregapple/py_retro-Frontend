import pygame, os, sys

from pygame.constants import QUIT, VIDEORESIZE
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from subprocess import SubprocessError
from py_retro.interactive import RetroEmu
from py_retro.core import *
from .display import *

config = configparser.ConfigParser()
config.read("./py_retro/settings/config.txt")
gameHistory = config['Last Opened Core / Game']
libpath = gameHistory['core']
rompath = gameHistory['game']

screen = Window()
pics = Images()
colors = Colors()
texts = Texts()
file = File()
PMenu = False



def Emulator():

    def PauseMenu():
        PMenu = True
        while PMenu == True:
            for x in pygame.event.get():
                if x.type == QUIT:
                    screen.display = 0
                    screen.exit()

                elif x.type == pygame.KEYDOWN:
                            if x.key == pygame.K_ESCAPE:
                                PMenu = False

                if x.type == VIDEORESIZE:
                    pygame.display.set_mode(x.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                    Window.resize() 
                    pics.__call__()
                    texts.__call__()
                    GameHistory().__call__()
                    texts.text1.__romtext__()
                    texts.text2.__coretext__()
                    screen.refresh()

            screen.tick(60)
            screen.displayScreen.blit(pics.bgR, (0, 0)) 

            Button(pics.w/(2560/2.7),pics.h/2.98,int(pics.w/3.6),int(pics.h/6.5),colors.red,colors.green,None,pics.Set,None, LoadGame) 
            Button(pics.w/(2560/2.2),pics.h/2.0175,int(pics.w/3.61),int(pics.h/7),colors.red,colors.green,None,pics.B3, None, None) 
            Button(pics.w/(2560/2),pics.h/1.54,int(pics.w/3.61),int(pics.h/7),colors.red,colors.green,None,pics.B2, None, None)
            Button(pics.w/(2560/2),pics.h/1.252,int(pics.w/3.58),int(pics.h/6.585),colors.red,colors.green,None,pics.Ex, None, screen.exit) 
            Button(pics.w/(2560/2078),pics.h/(2160/795),int(pics.w/12.925),int(pics.h/10.45),colors.red,colors.green,None,pics.F1, None, File.prompt1) 
            Button(pics.w/(2560/2073),pics.h/(2160/1138),int(pics.w/12.85),int(pics.h/10.5),colors.red,colors.green,None,pics.F2, None, File.prompt2) 
            Button(pics.w/(2560/938),pics.h/(2160/1470.5),int(pics.w/2.3107),int(pics.h/10.55),colors.red,colors.green,None,pics.Sg, None, NewGame) 
            GameHistory().__call__()
            texts.__call__()
            texts.text1.__romtext__()
            texts.text2.__coretext__()
            screen.refresh()

    def NewGame():
        global Game, running, PMenu, libpath, emu
        Game = False
        running = False
        emu.unload()
        emu.__del__()
        Main()

    def LoadGame():
        global libpath, rompath, emu
        emu = RetroEmu(libpath)
        load = True
        while load is True:
            with open(f'{rompath}.state', 'rb') as f:
                emu.unserialize(f.read())
                print('loaded state.')
                load = False
                pass
                



    def Main():
        global libpath, rompath, emu, Game, running
        config = configparser.ConfigParser()
        config.read("./py_retro/settings/config.txt")
        gameHistory = config['Last Opened Core / Game']
        libpath = gameHistory['core']
        rompath = gameHistory['game']
        # screen = Window.displayScreen
        Game = True

        while Game is True:

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
                        
                        if x.key == pygame.K_F2:
                            try:
                                with open(f'{rompath}.state', 'wb') as f:
                                    f.write(emu.serialize())
                                    print('saved state.')
                            except IOError:
                                print('could not write state.')
                        elif x.key == pygame.K_F4:
                            try:
                                with open(f'{rompath}.state', 'rb') as f:
                                    emu.unserialize(f.read())
                                    print('loaded state.')
                            except IOError:
                                print('could not read state.')
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
                        # elif event.key == pygame.K_v:
                        #     try:
                        #         with emu.av_record(f'{rompath}.webm', ['-c:v', 'libvpx-vp9']):
                        #             print('recording video, press ESC to end...')
                        #             while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        #                 emu.run()
                        #                 pygame.event.pump()
                        #             print('done recording video.')
                        #     except SubprocessError:
                        #         print('could not invoke ffmpeg.')
                        elif x.key == pygame.K_m:
                            quit()
                            # running = False
                            # mainMenu = True
                            # emu.unload()
                            # emu.__del__()
                            # menuMain()
                        # if fullscreen is False:
                        #     if pygame.key.get_pressed()[pygame.K_LALT] and pygame.key.get_pressed()[pygame.K_RETURN]:
                        #         fullscreen = True
                        #         pygame.display.set_mode((screenWidth, screenHeight))
                        #         pygame.display.flip()
                        #     else:
                        #         None
                                
                            
                                
                        # if fullscreen is True:
                        #     if pygame.key.get_pressed()[pygame.K_LALT] and pygame.key.get_pressed()[pygame.K_RETURN]:
                        #         fullscreen = False
                        #         pygame.display.set_mode((screenWidth, screenHeight))
                        #         pygame.display.flip()
                        #     else:
                        #         None
                                
                            # #emu.__del__()


                            
                            

    Main()