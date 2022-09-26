import numpy as np
import cv2
def cam():
	img = cv2.imread("/home/pi/Desktop/Elan.jpeg")
	kernel = np.ones((5,5),np.uint8)
	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	imgBlur = cv2.GaussianBlur(imgGray , (7,7),0)
	imgCanny = cv2.Canny (img, 150,200)
	imgDialation = cv2.dilate(imgCanny, kernel,iterations=1)
	imgEroded = cv2.erode(imgDialation,kernel,iterations =1)
	cv2.imshow("Gray Image ", imgGray)
	cv2.imshow("Blur Image" , imgBlur)
	cv2.imshow("Canny Image", imgCanny)
	cv2.imshow("Dialted Image",imgDialation)
	cv2.imshow("Eroded image", imgEroded)
if __name__ == "__main__":
#	try:
		while True:
				cam()
				if cv2.waitKey(1)& 0xFF == ord('q'):
					break
#	except:
#		cv2.destroyAllWindows()
