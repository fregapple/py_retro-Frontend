import configparser, itertools, os
import ctypes
import typing
from pathlib import Path
from py_retro.Frontend.configmake import core_settings
from py_retro.api.retro_ctypes import retro_variable

pyfolder = Path("./py_retro")
setfolder = Path("./py_retro/settings")
configFile = Path("./py_retro/settings/config.txt")
core_set_folder = Path("./Libretro Cores/Core Settings")



class CoreSettings:
    
    def core_identifier(env_vars, current, data):

        core_settings()
        if current.key == b'snes9x_region':
            key = str('snes9x_region')
            CoreSettings.snes9x(env_vars, data, key)

        elif current.key == b'vbanext_bios':
            key = str('vbanext_bios')
            CoreSettings.vbaNext(env_vars, data, key)
        
        elif current.key == b'parallel-n64-cpucore':
            key = str('parallel-n64-cpucore')
            CoreSettings.paralell(env_vars, data, key)
                   
        elif current.key == b'gambatte_gb_colorization':
            key = str('gambatte_gb_colorization')
            CoreSettings.gambatte(env_vars, data, key)
                    
        else: 
            CoreSettings.default_settings(env_vars, data)

    def default_settings(env_vars, data):
        variables = ctypes.cast(data, ctypes.POINTER(retro_variable))
        idx = 0
        current = variables[idx]
        while current.key is not None:
            description, _, options = current.value.partition(b'; ')
            options = options.split(b'|')
            val = env_vars.setdefault(current.key, options[0])
            assert val in options, f'{val} invalid for {current.key}, expected {options}'
            idx += 1
            current = variables[idx]
            print(val)
        
   
('C:/Users/sam_s/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/pygame_gui/data', 'pygame_gui/data'),