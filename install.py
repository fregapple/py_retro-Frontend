from setuptools import sandbox
import shutil, subprocess, sys


def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])

sandbox.run_setup('setup.py', ['build'])
install()
shutil.rmtree('./build')
shutil.rmtree('./temp')
shutil.rmtree('./Py_Retro_Frontend.egg-info')