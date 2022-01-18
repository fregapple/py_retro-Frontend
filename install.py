from setuptools import sandbox
import shutil, subprocess, sys, os, pip, glob

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
try:
    shutil.copytree('./src/Libretro Cores', './Frontend/Libretro Cores')
except:
    print('folder already exists')
try:
    shutil.move('./dist/Frontend2.exe', './Frontend')
except:
    print('folder already exists')
shutil.rmtree('./build')
shutil.rmtree('./dist')