# -*- mode: python ; coding: utf-8 -*-

import sys

block_cipher = None

citramanik_runtime_hooks = [
	'pyinstaller/fontconfig_hook.py',
	'pyinstaller/qtplatform_hook.py'
]

a = Analysis(['citramanik/main.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=citramanik_runtime_hooks,
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

if sys.platform == "darwin":
    exe = EXE(pyz,
            a.scripts,
            a.binaries,
            a.zipfiles,
            a.datas,
            [],
            name='citramanik-qt',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=True , icon='icons/Icon.icns')
    app = BUNDLE(
        exe,
        name='citramanik-qt.app',
        author='Devlovers ID',
        version='1.3.2',
        bundle_identifier='id.devlovers.citramanik-qt',
        info_plist={
	    'NSPrincipalClass': 'NSApplication',
            'LSBackgroundOnly': False,
	    'NSAppleScriptEnabled': False,
            'NSHighResolutionCapable': True
        },
        icon='icons/Icon.icns'
    )
else:
    exe = EXE(pyz,
            a.scripts,
            a.binaries,
            a.zipfiles,
            a.datas,
            [],
            name='Citramanik',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=True , icon='icons/Icon.ico')
