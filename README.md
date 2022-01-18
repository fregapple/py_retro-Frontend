This is a continuation of works I have found on GitHub, - https://github.com/lifning/python-retro -

I am new to coding, and using this as a difficult / challenging way to learn. I stop frequently to look up how to do certain things, not to mention the main file for the Frontend is just STACKED with code. A lot is unnecessary, but currently works.

This is just a project for myself and sharing on GitHub for anyone to checkout and give advice!

Please know, as I said, the code is a mess and I have started making new main files utilising classes a bit more. And I will end up rewriting many times as I learn new ways to organise and structure the code.

All in all, you are able to load games and run N64, SNES/NES and GB/GBC/GBA. Once I learn how to implement more cores and maybe add in OpenGL support for HW rendering I will start to shift to add more to Lifning's code. But right now I have added a few lines to their code so you are able to adjust the window size, either via dragging the window, or editing the config file.

##### Have made a few changes from the original. Firstly, I have incorporated pygame_gui, so I can use their library of UI elements, rather than creating them myself. I will eventually change the menu buttons to reflect this change. In turn, I have removed TKINTER as I am using pygame_gui's file dialog now.

##### You can now save and change core settings!!! This is a very basic implementation and want to have the option to change these settings within the Frontend. However, for now you have to change the value within the txt file.




**To Install:**

You either download the release that I have packaged myself.

Or you can package it yourself with the code.

To do so, download my code and Lifnings code. Drag Lifning's code into the src folder of mine and don't overwrite the files, as I have adjusted certain things to hack em together. Then go back to main directory and run: python install.py in CMD.

This installer will also download all the dependencies needed with pip: pygame_gui, pygame, pyinstaller. And it will attempt to install pyaudio from the folder included in ./src. The pyaudio files included in the folder are 32 / 64 bit specific for windows, you'll have to install your own version of pyaudio independently if running another OS. I have done so on linux with 'sudo apt-get python-pyaudio'.

_There are a few issues with certain versions of python and various methods of packaging:_

Python3.6 will package it fine however it will not run any game due to the 32bit - 64bit converter I have implemented for the logging

Python3.9.5 will not package and run into an error of decoding. 

Python3.9.9 from the windows store works well

Python3.10_32 works well as well! In fact with some cores it isn't missing some of the log information. I think for the 64 bit versions, my converter loses some data.

Python3.6_64 and above on linux seems to run well and as the code doesn't need the converter unlike windows, there is no missing logs either.

Haven't tried other versions of python

FIX: Delete the CEXT file in './src/py_retro' and run the Frontend2.py in src with cmd. The cext file is only used for logging so for playing is not needed
