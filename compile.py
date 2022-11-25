#!/usr/bin/env python3
import os
from sys import platform

src = "src/app.py"
name = "pbrain-gomoku-ai.exe"

os.system("pip3 install pyinstaller")
os.system("python3 -m PyInstaller --onefile " + src + " --name " + name)
print(platform)
if (platform == 'win32'):
    os.system('copy .\\dist\\pbrain-gomoku-ai.exe .')
elif (platform == 'linux'):
    os.system('cp ./dist/pbrain-gomoku-ai.exe .')
