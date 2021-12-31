#!/usr/bin/env python3.6
from setuptools import setup, Extension

cext = Extension('Test.py_retro.cext', sources = ['./Test/c_ext_src/log_wrapper.c'])

setup(name='Py_Retro Frontend',
      version='0w0',
      description='Frontend for Lifnings project.',
      packages=[
          'Test',
          'Test.examples',
          'Test.py_retro',
          'Test.py_retro.api',
          'Test.py_retro.interactive',
          'Test.py_retro.recording',
          'Test.py_retro.tas',
          'Test.py_retro.settings',
          'Test.py_retro.Frontend',    
      ],
      package_data={'./Test/py_retro/settings': ['*.png', '*.txt']},
      include_package_data=True,
      ext_modules=[cext]
      )
