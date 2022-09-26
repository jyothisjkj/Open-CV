import picamera

import time

camera = picamera.PiCamera()

camera.vflip = True

camera.start_recording('/home/pi/Desktop/examplevid.h264')

time.sleep(5)

camera.stop_recording


