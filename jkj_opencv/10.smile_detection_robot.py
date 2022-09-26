
import cv2
import numpy as np
import imutils
from imutils.video import VideoStream
import move
import time
usingPiCamera = True
frameSize = (320, 240)
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
		framerate=32).start()
time.sleep(2.0)
image_width = 320
image_height = 240

def cam():
	while True:
		img = vs.read()
		image = cv2.flip(img, 0)
		smile_cascade = cv2.CascadeClassifier('/home/pi/opencv_new/haar-cascade-files/haarcascade_smile.xml')
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		smiles  = smile_cascade.detectMultiScale(gray, 1.8,20)
		smile_x = 0
		move.stop()
		print("stop")
		for (x,y,w,h) in smiles:
			cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)
			width = w
			height = h
			center_x = x + (width / 2)
			smile_x = center_x
			if smile_x > 170:
				move.left(80)
				print ("left")
			elif smile_x < 130:
				move.right(80)
				print ("right")
			elif smile_x>130 and smile_x<170:
				move.forward(80)
				print ("forward")
			else:
				move.stop()
				print ("stop")
		cv2.imshow("frame",image)
		key = cv2.waitKey(1)
		if key == ord("q"):
			break

if __name__ == "__main__":
	try:

		cam()
	except:
		cv2.destroyAllWindows()
		vs.stop()
		move.stop() 
