
from setuptools import setup, Extension

cext = Extension('src.py_retro.cext', sources = ['./src/c_ext_src/log_wrapper.c'])

setup(name='Py_Retro Frontend',
      version='1.0',
      description='Frontend for Lifnings project.',
      packages=[
          'src',
          'src.examples',
          'src.py_retro',
          'src.py_retro.api',
          'src.py_retro.interactive',
          'src.py_retro.recording',
          'src.py_retro.tas',
          'src.py_retro.settings',
          'src.py_retro.src',    
      ],
      package_data={'./src/py_retro/settings': ['*.png', '*.txt']},
      include_package_data=True,
      ext_modules=[cext]
      )

