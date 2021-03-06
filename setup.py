"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['suffer.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'if_smiley__20_2290998.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
