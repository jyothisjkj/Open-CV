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
#center_image_x = image_width / 2
#center_image_y = image_height / 2
#minimum_area = 250
#maximum_area = 100000
#def _map(object_x,in_min,in_max,out_min,out_max):
#	return int((object_x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min)
def cam():
	while True:
		img = vs.read()
		image = cv2.flip(img, 0)
		face_cascade = cv2.CascadeClassifier('/home/pi/opencv_new/haar-cascade-files/haarcascade_frontalface_alt.xml')
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
		faces  = face_cascade.detectMultiScale(gray, 1.3,2) 
		face_x = 0
		move.stop()
		print ("stop")
		for (x,y,w,h) in faces:
			cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)
			width = w
			height = h
			center_x = x + (width / 2)
			face_x = center_x
			print ("face_x:",face_x)
			if face_x > 170:
				move.left(80)
				print ("left")
			elif face_x <130:
				move.right(80)
				print ("right")
			elif face_x>130 and face_x<170:
				move.forward(80)
				print ("forward")
			else:
				move.stop()
				print ("stop") 

			#	face_y = center_y
		#if face_area > 0:
		#	face_location = [face_area, face_x, face_y]
		#else:
		#	face_location = None

		#if face_location:
		#	if (face_location[0] > minimum_area) and (face_location[0] < maximum_area):
		#		if face_location[1] > (center_image_x + (image_width/3)):
		#			move.right(60)
		#			print("Turning right")
		#		elif face_location[1] < (center_image_x - (image_width/3)):
		#			move.left(60)
		#			print("Turning left")
		#		else:
		#			move.forward(80)
		#			print("forward1")
		#	elif (face_location[0] < minimum_area):
		#		move.stop()
		#		print("stop2")
		#	else:
		#		move.stop()
		#		print("stop")
	#	else:
	#		move.stop()
	#		print("stop")
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

