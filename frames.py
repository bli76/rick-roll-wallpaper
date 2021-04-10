# Run this script first to populate the frames folder
# The mp4 file can be deleted afterward
# Libraries need to be installed using pip

import cv2 as cv
import youtube_dl as ydl

# Download video from YouTube URL
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ydl_opts = {'outtmpl': 'video.mp4'}
dl.YoutubeDL(ydl_opts).download([link])

# Read the mp4 file
cam = cv.VideoCapture('video.mp4')
currentframe = 0
  
# Extract every frame
while(True):

    ret, frame = cam.read()
  
    if ret:
        name = './frames/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        cv.imwrite(name, frame)
  
        currentframe += 1
    else:
        break