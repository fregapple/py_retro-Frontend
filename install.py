from setuptools import sandbox
import shutil, subprocess, sys, os, pip, glob, pathlib, platform, struct

def packagepygame():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame", "-U"])

def packagepygame_gui():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame_gui", "-U"])

def packagepyinstaller():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "-U"])

def packagecext():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])

def install():
    subprocess.check_call(["pyinstaller", "--onefile", "./src/Frontend2.spec"])


for path in glob.glob("./src/pyaudio.wheels/*.whl"):
    pip.main(['install',path])

packagepygame()
packagepygame_gui()
packagepyinstaller()

sandbox.run_setup('setup.py', ['build'])

packagecext()

for pyd in pathlib.Path('./src/py_retro').glob('*.pyd'):
    shutil.copy(pyd, './src/py_retro/cext.pyd') 

for so in pathlib.Path('./src/py_retro').glob('*.so'):
    shutil.copy(so, './src/py_retro/cext.so')


shutil.rmtree('./build')
shutil.rmtree('./temp')
shutil.rmtree('./Py_Retro_Frontend.egg-info')

install()



try:
    os.mkdir('./Frontend')
except:
    print('folder already exists')
try:
    os.mkdir('./Frontend/Games')
except:
    print('folder already exists')

try:
    shutil.copytree('./src/examples','./Frontend/examples')
except:
    print('folder already exists')

if platform.system() == 'Windows' and struct.calcsize("P")*8 == 32:
    print("py_retro Windows-32bit Version Installed")
    try:
        shutil.copytree('./src/Libretro Cores/win32', './Frontend/Libretro Cores')
    except:
        print('folder already exists')

elif platform.system() == 'Windows' and struct.calcsize("P")*8 == 64:
    try:
        shutil.copytree('./src/Libretro Cores/win64', './Frontend/Libretro Cores')
    except:
        print('folder already exists')

elif platform.system() == 'Linux' and struct.calcsize("P")*8 == 64:
    try:
        shutil.copytree('./src/Libretro Cores/linux64', './Frontend/Libretro Cores')
    except:
        print('folder already exists')

try:
    shutil.move('./dist/Frontend2.exe', './Frontend')
except:
    print('folder already exists')

shutil.rmtree('./build')
shutil.rmtree('./dist')