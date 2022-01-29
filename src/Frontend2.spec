# -*- mode: python ; coding: utf-8 -*-
import os, pygame_gui
pygame_data_loc = os.path.join(os.path.dirname(pygame_gui.__file__), 'data')


block_cipher = None


a = Analysis(['Frontend2.py'],
             pathex=[],
             binaries=[('./py_retro/cext.cp39-win_amd64.pyd','./py_retro')],
             datas=[('./py_retro/Frontend/*','./py_retro/Frontend'), 
		    ('./py_retro/interactive/*', './py_retro/interactive'),
		    ('./py_retro/api/*', './py_retro/api'),
		    ('./py_retro/recording/*', './py_retro/recording'),
		    ('./py_retro/tas/*', './py_retro/tas'),
		    ('./py_retro/__init__.py', './py_retro'),
		    ('./py_retro/core.py', './py_retro'),
		    ('./py_retro/game_info_reader.py', './py_retro'),
		    (pygame_data_loc, "pygame_gui/data"),
		    ('./data/themes/*', './data/themes'),
		    ('./data/fonts/*', './data/fonts'),
		    ('./data/images/*', './data/images')],
             hiddenimports=['pyaudio', 'pygame_gui'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Frontend2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
