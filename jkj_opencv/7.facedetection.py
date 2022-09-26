import cv2

def cam(): 

	faceCascade= cv2.CascadeClassifier('/home/pi/opencv_new/haar-cascade-files/haarcascade_frontalcatface.xml')

	img = cv2.imread('/home/pi/opencv_new/messi.jpeg')

	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

 

	faces = faceCascade.detectMultiScale(imgGray,1.3,5)

 

	for (x,y,w,h) in faces:

		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

 

		cv2.imshow("Result", img)

if __name__ == "__main__":

    try:

        while True:         

            cam()

            if cv2.waitKey(1)  == ord('q'):

                    break

    except:

        cv2.destroyAllWindows()


