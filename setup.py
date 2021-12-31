#!/usr/bin/env python3.6
from setuptools import setup, Extension

cext = Extension('Frontend.py_retro.cext', sources = ['./Frontend/c_ext_src/log_wrapper.c'])

setup(name='Py_Retro Frontend',
      version='0w0',
      description='Frontend for Lifnings project.',
      packages=[
          'Frontend',
          'Frontend.examples',
          'Frontend.py_retro',
          'Frontend.py_retro.api',
          'Frontend.py_retro.interactive',
          'Frontend.py_retro.recording',
          'Frontend.py_retro.tas',
          'Frontend.py_retro.settings',
          'Frontend.py_retro.Frontend',    
      ],
      package_data={'./Frontend/py_retro/settings': ['*.png', '*.txt']},
      include_package_data=True,
      ext_modules=[cext]
      )

