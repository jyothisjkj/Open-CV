import time

import cv2

import numpy as np

from imutils.video import VideoStream

import imutils

 

usingPiCamera = True

frameSize = (320, 240)

vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,

		framerate=32).start()

time.sleep(2.0)

while True:

	image = vs.read()

	frame = cv2.flip(image, 0)

	cv2.imshow('orig', frame)

	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):

		break



cv2.destroyAllWindows()

vs.stop()


