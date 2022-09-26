import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import time
def nothing(x):
	print (x)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("B", "Trackbars", 0, 255,nothing)
cv2.createTrackbar("G", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("R", "Trackbars", 0, 255, nothing)
usingPiCamera = True
frameSize= (640,320)
vs =  VideoStream (src =0, usePiCamera = usingPiCamera , resolution = frameSize , framerate =32).start()
time.sleep(2.0)
while True:
	global Blue
	img = vs.read()
	image = cv2.flip(img, 0)
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	B = cv2.getTrackbarPos("B", "Trackbars")
	G = cv2.getTrackbarPos("G", "Trackbars")
	R = cv2.getTrackbarPos("R", "Trackbars")
	green = np.uint8([[[B, G, R]]])
	hsvGreen = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
	lowerLimit = np.uint8([hsvGreen[0][0][0]-10,100,100])
	upperLimit = np.uint8([hsvGreen[0][0][0]+10,255,255])
	mask = cv2.inRange(hsv, lowerLimit, upperLimit)
	result = cv2.bitwise_and(image, image, mask=mask)
	cv2.imshow("frame", image)
	cv2.imshow("mask", mask)
	cv2.imshow("result", result)
	key = cv2.waitKey(1)
	if key == 27:
		break
cv2.destroyAllWindows()
vs.stop()




