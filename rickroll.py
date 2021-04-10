# PIL and playsound libraries need to be installed via pip

# Audio file should be pre-downloaded using a third-party
# website with the name audio.mp3 and place in the same directory
# as this script

from PIL import Image
from os import getenv, system
import playsound as ps
import threading as thr

def playVid():
    system('wallpaper.exe')

def vidThread():
    th = thr.Thread(target=playVid)
    th.start()

def playSound():
    ps.playsound('audio.mp3')

def soundThread():
    th = thr.Thread(target=playSound)
    th.start()

# Save the current wallpaper
currentWallpaper = getenv('APPDATA') + '/Microsoft/Windows/Themes/TranscodedWallpaper'
img = Image.open(currentWallpaper)
img.save('wallpaper.png')

# Run the compiled C++ code
# and play the audio file
# on separate threads
vidThread()
soundThread()

# Python to EXE: https://www.geeksforgeeks.org/convert-python-script-to-exe-file/