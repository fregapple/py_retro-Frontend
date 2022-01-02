from pathlib import Path
import configparser, os


pyfolder = Path("./py_retro")
setfolder = Path("./py_retro/settings")
configFile = Path("./py_retro/settings/config.txt")

if pyfolder.is_dir():
    None

else: 
    os.mkdir('./py_retro') 

if setfolder.is_dir():
    None
else: 
    os.mkdir('./py_retro/settings')
    
if configFile.is_file():
    None

else:
    config = configparser.ConfigParser()
    config['Display Settings'] = {'Resolution Width': 800,
                                  'Resolution Height': 600,
                                                            }
    config['Something'] = {}
    config['Something']['User'] = 'FregApple'
    config['Last Opened Core / Game'] = {}
    topsecret = config['Last Opened Core / Game']
    topsecret['Core'] = 'Core'  
    topsecret['Game'] = 'Rom'
    with open("./py_retro/settings/config.txt", "w") as configfile:
        config.write(configfile)

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

    
    