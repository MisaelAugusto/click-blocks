from cx_Freeze import setup, Executable
import sys
import pygame

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("game.py", base=base)]

packages = ["pygame"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Click Blocks",
    options = options,
    version = "1.0",
    description = 'Click on Blocks more fast you can!',
    executables = executables
)
