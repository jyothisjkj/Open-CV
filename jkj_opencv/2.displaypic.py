import numpy as np
import cv2
def cam():
	img = cv2.imread('/home/pi/Desktop/image5.jpg')
	cv2.imshow('image',img)

if __name__ == "__main__":
	try:
		while True:
			cam()
			if cv2.waitKey(1) & 0xFF ==  ord('q'):
				break
	except:
		cv2.destroyAllWindows()
