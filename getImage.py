# @brief: Script is written for the purpose of the AutoHack18 competition 
# by the OpenWorks Team. Script is based on the picamera module and 
# example available here: 
# http://picamera.readthedocs.io/en/release-1.13/recipes1.html

from time import sleep
from time import strftime
from picamera import PiCamera

# Setup the camera object
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

# Create a name string for the image
assetUID = "HT3"
timeStr  = strftime("_%Y%m%d_%H%M%S")
imageExt = ".jpg"
imageStr = assetUID + timeStr + imageExt 

# Camera warm-up time
sleep(2)
camera.capture(imageStr)

# Send image to OpenWorks DB
