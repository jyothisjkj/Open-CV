import time
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import move
import warnings
import math
usingPiCamera = True
frameSize = (640, 480)
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,framerate=32).start()
time.sleep(2.0)
theta=0
minLineLength = 5
maxLineGap = 10
def _map(value,in_min,in_max,out_min,out_max):
        return float((value-in_min)*(out_max-out_min)/(in_max-in_min)+out_min)
while True:
	frame = vs.read()
	vertical_flip = cv2.flip(frame, 0)
	output_image = cv2.flip(vertical_flip, 1)
	gray=cv2.cvtColor(output_image,cv2.COLOR_RGB2GRAY)
	blur=cv2.GaussianBlur(gray, (5,5), 0)
	canny=cv2.Canny(blur,50,150)
	height=canny.shape[0]
	width=canny.shape[1]
	region = np.array([[(0, height),(0,  height/2),(width , height/2),(width , height),]], np.int32)
	mask=np.zeros_like(canny)
	fill =cv2.fillPoly(mask,region, 255)
	roi_image =cv2.bitwise_and(canny,mask)
	lines = cv2.HoughLinesP(roi_image,1,np.pi/180,10,minLineLength,maxLineGap)
	if lines is not None:
		for x in range(0, len(lines)):
			for x1,y1,x2,y2 in lines[x]:
				cv2.line(output_image,(x1,y1),(x2,y2),(0,255,0),2)
				theta=theta+math.atan2((y2-y1),(x2-x1))
				print("theta",theta)
	threshold=2
	if(theta >threshold):
		left_value  = _map(theta,0,30,90,180)
		print ("l",left_value)
		left = 180 #  left_value
		move.steering(70,left)
		print("left",left)
	if(theta <- threshold):
		right_value = _map(abs(theta),0,30,90,0)
		print ("r",right_value)
		right = 0  # right_value
		move.steering(70,right)
		print("right",right)
	if(abs(theta)<threshold):
		move.steering(70,90)
	theta=0
	cv2.imshow('canny',canny)
	cv2.imshow('roi',roi_image)
	cv2.imshow('orig', output_image)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()
move.stop()

