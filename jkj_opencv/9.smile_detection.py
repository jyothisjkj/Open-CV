import time
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
# Are we using the Pi Camera?
usingPiCamera = True
# Set initial frame size.
frameSize = (320, 240)
 
# Initialize mutithreading the video stream.
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
		framerate=32).start()
# Allow the camera to warm up.
time.sleep(2.0)
#capture frames from the camera
while True:
    img =vs.read()        #Load a cascade file for detecting faces
    image =cv2.flip(img,0)
    smile_cascade = cv2.CascadeClassifier('/home/pi/opencv_new/haar-cascade-files/haarcascade_smile.xml')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #Convert to grayscale
    smiles = smile_cascade.detectMultiScale(gray, 1.8, 30) #Look for faces in the image using the loaded cascade file
    for (x,y,w,h) in smiles:   #Draw a rectangle around every found face
        print (x,y,w,h)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)  #face detected
    cv2.imshow("Frame",image)  #show the frame
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
vs.stop()

