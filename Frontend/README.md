This is a continuation of works I have found on GitHub, - https://github.com/lifning/python-retro -

I am new to coding, and using this as a difficult / challenging way to learn. I stop frequently to look up how to do certain things, not to mention the main file for the Frontend is just STACKED with code. A lot is unnecessary, but currently works. I did break the resolution settings as I added a new GUI and made it scale with VIDEORESIZABLE. So my old resolution options don't work correctly. I also have kept my old buttons for loading a core / rom. However they will be changed to match the theme.. eventually!

This is just a project for myself and sharing on GitHub for anyone to checkout and give advice!

Please know, as I said, the code is a mess and I have started making new main files utilising classes a bit more. And I will end up rewriting many times as I learn new ways to organise and structure the code.

All in all, you are able to load games and run N64, SNES/NES and GB/GBC. Once I learn how to implement more cores and maybe add in OpenGL support for HW rendering I will start to shift to add more to Lifning's code. But right now I have added a few lines to their code so you are able to adjust the window size, either via dragging the window, or editing the config file.

To install.

You'll have to have python and pygame installed to run this currently until it is further developed and I make an exe. download Lifning's code from their GitHub, then drag and drop the contents of mine into theirs. Replace all the files it requests as it provides the scaling hacks for resolution. The more update to date file to run is Frontend2.py

If you want, you can also use the setup.py script to install the cext file to enable logging. However, for general usage it isn't needed.

I have included 3 of Libretro's cores that work for the above mentioned systems. You'll need to provide your own roms.
