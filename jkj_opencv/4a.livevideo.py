from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))
for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
	image = frame.array
	frame = cv2.flip(image,0)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1)& 0xFF
	rawCapture.truncate(0)
	if key == ord("q"):
		break
cv2.destroyAllwindows()

