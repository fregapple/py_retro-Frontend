from setuptools import sandbox
import shutil, subprocess, sys, os


def packagecext():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])

def install():
    subprocess.check_call(["pyinstaller", "--onefile", "./Test/Frontend2.spec"])

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