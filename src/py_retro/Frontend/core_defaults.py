import os, sys, pygame, configparser
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
        self.bg = self.cd['.gb']
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
    def coreWrite(corename, extension):
        config.read(conRead) 
        config.set('Core Defaults', f'{extension}', f'{corename}')     
        with open(conRead, "w") as configfile:
            config.write(configfile)
            config.read(conRead)

    # A call to change Core Defaults. 
    # FIXME: This needs to be changed as it prevents applying default cores for individual systems. 
            # EG: bsnes for snes and snes9x for nes and vice versa.
    def defaultChange(file_name, corename):
        config.read(conRead)
        print(file_name)
        print(corename)
        if file_name == 'gambatte_libretro':
            extension = '.gbc'
            CoreDefaults.coreWrite(corename, extension)
        
        elif file_name == 'bsnes_libretro': 
            extension = '.snes'
            CoreDefaults.coreWrite(corename, extension)

        elif file_name == 'snes9x_libretro':
            extension = '.snes'
            CoreDefaults.coreWrite(corename, extension)




           



        


