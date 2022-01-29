from __future__ import nested_scopes
import os, sys, pygame, configparser

import pygame_gui
from py_retro.Frontend.configmake import *

# Global information for ease
config = configparser.ConfigParser()
conRead = "./py_retro/settings/config.txt"
config.read(conRead)
CD = config['Core Defaults']

# As defined, Core Default class.
class CoreDefaults():

    def __init__(self):
        self.__call__()

    def __call__(self):
        self.config = configparser.ConfigParser()
        self.config.read("./py_retro/settings/config.txt")
        self.cd = self.config['Core Defaults']
        self.active = self.cd['active core']
        self.gbc = self.cd['.gbc']
        self.gb = self.cd['.gb']
        self.gba = self.cd['.gba']
        self.nes = self.cd['.nes']
        self.snes = self.cd['.snes']
        self.n64 = self.cd['.n64']
    
    # Checks which rom is loaded for what system and will select the appropriate Core as Active Core
    def coreCheck(file_extension):
        config = configparser.ConfigParser()
        config.read("./py_retro/settings/config.txt")
        if file_extension == '.gbc':
            active = CoreDefaults().gbc
            return active
        elif file_extension == '.z64':
            active = CoreDefaults().n64
            return active
        elif file_extension == '.gba':
            active = CoreDefaults().gba
            return active
        elif file_extension == '.smc':
            active = CoreDefaults().snes
            return active

    # A fuction that can be used by the defaultChange to declutter and write new Defaults to the config file.
    def coreWrite(corename, extension, extension2, extension3):
        config.read(conRead) 
        config.set('Core Defaults', f'{extension}', f'{corename}')
        if extension2 is not None:
            config.set('Core Defaults', f'{extension2}', f'{corename}')
        if extension3 is not None:
            config.set('Core Defaults', f'{extension3}', f'{corename}')     
        with open(conRead, "w") as configfile:
            config.write(configfile)
            config.read(conRead)

    # A call to change Core Defaults. 
    # FIXME: This needs to be changed as it prevents applying default cores for individual systems. 
            # EG: bsnes for snes and snes9x for nes and vice versa.
    def defaultChange(file_name, corename):       
        print(file_name)
        print(corename)
        if file_name == 'gambatte_libretro':
            extension = '.gbc'
            extension2 = '.gb'
            CoreDefaults.coreWrite(corename, extension, extension2, None)
        
        elif file_name == 'bsnes_libretro': 
            extension = '.snes'
            extension2 = '.nes'
            CoreDefaults.coreWrite(corename, extension, extension2, None)

        elif file_name == 'snes9x_libretro':
            extension = '.snes'
            extension2 = '.nes'
            CoreDefaults.coreWrite(corename, extension, extension2, None)


    def specificCoreChange(file_name, corename, manager, size):
        from .display import DefaultSelector
        if file_name == 'gambatte_libretro':
            item1 = '.gb'
            item2 = '.gbc'
            item3 = None
        rect = pygame.Rect((0,0),(250,175))
        rect.center = size[2].get_rect().center
        DefaultSelector(rect, manager, item1, item2, item3, corename) 

           



        


