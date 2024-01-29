# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None
hiddenimports = []
hiddenimports += collect_submodules('sklearn')
hiddenimports += collect_submodules('numpy')
hiddenimports += collect_submodules('tensorflow')

a = Analysis(
    ['cnn_train.py'],
    pathex=['../.conda/Lib/site-packages', 'C:\Windows\System32\downlevel'],
    binaries=[('../.conda/Lib/site-packages/tensorflow/python/_pywrap_tensorflow_internal.pyd', '.')],
    datas=[('../.conda/Lib/site-packages/tensorflow/python/_pywrap_tensorflow_internal.pyd', '.')],
		hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='cnn_train',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='cnn_train',
)
