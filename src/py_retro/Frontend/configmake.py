from pathlib import Path
import configparser, os

# Global definitions for ease
pyfolder = Path("./py_retro")
setfolder = Path("./py_retro/settings")
configFile = Path("./py_retro/settings/config.txt")
core_set_folder = Path("./Libretro Cores/Core Settings")

# The below if and else options look for directories and if they don't exist will make them.
if pyfolder.is_dir():
    None

else: 
    os.mkdir(pyfolder) 

if setfolder.is_dir():
    None
else: 
    os.mkdir(setfolder)

def core_settings():
    
    if core_set_folder.is_dir():
        None
    else:
        os.mkdir(core_set_folder)

# This looks for the config file. If it doesn't exits it will make it with the below parameters. 
if configFile.is_file():
    None

else:
    config = configparser.ConfigParser()
    config['Display Settings'] = {'Resolution Width': 800,
                                  'Resolution Height': 600,
                                                            }
    config['Core Defaults'] = {}
    config['Core Defaults']['active core'] = 'None'
    config['Core Defaults']['.gbc'] = './Libretro Cores/gambatte_libretro.dll'
    config['Core Defaults']['.gb'] = './Libretro Cores/gambatte_libretro.dll'
    config['Core Defaults']['.gba'] = './Libretro Cores/vba_next_libretro.dll'
    config['Core Defaults']['.nes'] = './Libretro Cores/snes9x_libretro.dll'
    config['Core Defaults']['.snes'] = './Libretro Cores/snes9x_libretro.dll'
    config['Core Defaults']['.n64'] = './Libretro Cores/parallel_n64_libretro.dll'
    config['Last Opened Core / Game'] = {}
    topsecret = config['Last Opened Core / Game']
    topsecret['Core'] = 'Core'  
    topsecret['Game'] = 'Rom'
    with open("./py_retro/settings/config.txt", "w") as configfile:
        config.write(configfile)


# Similar to the config file, it will create the ReadMe file if it doesn't exist.
class ReadMe():
    readmeFile = Path("./py_retro/settings/README.txt")
    if readmeFile.is_file():
        None

    else:
        readme = configparser.ConfigParser(allow_no_value=True)
        readme['_####################################################################################################_'] = {}
        readme["___________________________________Welcome to py_retro's Frontend_____________________________________"] = {}
        readme['######################################################################################################'] = {}
        readme.set('######################################################################################################', '; Hi there! I have been working on a frontend for this project I found on GitHub. I have no ownership')
        readme.set('######################################################################################################', "; over lifning's python-retro project. I am a fan of what he was attempting to achieve even though") 
        readme.set('######################################################################################################', '; he seems to have halted work on the project 3 years ago.') 
        readme.set('######################################################################################################', '; ') 
        readme.set('######################################################################################################', '; I am new to all this and my code is MESSY as anything. But I am using this as a learning project') 
        readme.set('######################################################################################################', '; for my self. I am not sure how far I will be able to take it, but I have really enjoyed the challenge') 
        readme.set('######################################################################################################', '; so far!')  
        readme.set('######################################################################################################', '; This project is first aiming to create a functional frontend that will transition seemlessly. This')
        readme.set('######################################################################################################', '; is because the original project only utilises CMD commands to open and run the systems.')
        readme.set('######################################################################################################', '; ') 
        readme.set('######################################################################################################', '; ')  
        readme.set('######################################################################################################', '; ') 
        readme.set('######################################################################################################', '; Thanks for following me and checking out this project! Please be sure to check out the original') 
        readme.set('######################################################################################################', '; code from: https://github.com/lifning/python-retro') 
        readme['______________________________________________________________________________________________________'] = {}
        with open("./py_retro/settings/README.txt", "w") as readmefile:
            readme.write(readmefile)

class ConfigRead:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.OpenFile()

    def OpenFile(self):
        return self.config.read("./py_retro/settings/config.txt")

    def DisplayRead(self):
        DisplaySettings = self.config['Display Settings']
        return (int(DisplaySettings['resolution width']), int(DisplaySettings['resolution height']))

    def DisplayWrite(self, w, h):
        self.config.set('Display Settings', 'resolution width', f'{w}')
        self.config.set('Display Settings', 'resolution height', f'{h}')
        with open("./py_retro/settings/config.txt", "w") as configfile:
            self.config.write(configfile)
            self.OpenFile()
            DisplaySettings = self.config['Display Settings']
            return (int(DisplaySettings['resolution width']), int(DisplaySettings['resolution height']))
    
    def GameWrite(self, core, rom, activecore):
        if core is not None:
            self.config.set('Last Opened Core / Game', 'core', f'{core}')
        if rom is not None:
            self.config.set('Last Opened Core / Game', 'game', f'{rom}')
        if activecore is not None:
            self.config.set('Core Defaults', 'active core', f'{activecore}')
        with open("./py_retro/settings/config.txt", "w") as configfile:
            self.config.write(configfile)
            self.OpenFile()

    def GameRead(self):
        self.gh = self.config['Last Opened Core / Game']
        self.Ga = self.gh['game']
        self.Co = self.gh['core']
        return (self.Ga, self.Co)
    
