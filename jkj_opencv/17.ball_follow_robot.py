# import the necessary packages
import cv2
import numpy as np
import imutils
from imutils.video import VideoStream
import move
import time 
# initialize the camera and grab a reference to the raw camera capture
usingPiCamera = True
# Set initial frame size.
frameSize = (320, 240)
 
# Initialize mutithreading the video stream.
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
        framerate=32).start()
# Allow the camera to warm up.
time.sleep(2.0)
image_width = 320
image_height = 240
center_image_x = image_width / 2
center_image_y = image_height / 2
minimum_area = 250
maximum_area = 100000
 
#we can find out the lower and upper limit of color in  hsv
lower_color = np.array([15,100,100])
upper_color = np.array([40, 255, 255])
def cam(): 
#try:
#capture continuos unction to start reading the frames from the raspberry pi camera module
  while True:
    img = vs.read()
    image = cv2.flip(img, 0)
 #now we are going to convert images from the bgr to hsv color space 
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 #we adjust the threshold of the hsv image for a range of each selected color. 
    color_mask = cv2.inRange(hsv,lower_color, upper_color)
 
    _ ,countours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    countours=sorted(countours,key=lambda x:cv2.contourArea(x),reverse=True) 
    object_area = 0
    object_x = 0
    object_y = 0
  
    #to find the  object area
    for contour in countours:
        for cnt in countours:
          (x,y,w,h)=cv2.boundingRect(cnt)
          x_medium = int((x + x + w) / 2)
          cv2.line(image,(x_medium,0),(x_medium,480),(0,255,0),2)
          break

        x, y, width, height = cv2.boundingRect(contour)
        found_area = width * height
        center_x = x + (width / 2)
        center_y = y + (height / 2)
        
        if object_area < found_area:
           object_area = found_area
           object_x = center_x
           object_y = center_y
# object location detect
    if object_area > 0:
        ball_location = [object_area, object_x, object_y]
        print (ball_location)
    else:
        ball_location = None
 
    if ball_location:
        if (ball_location[0] > minimum_area) and (ball_location[0] < maximum_area):
            if ball_location[1] > (center_image_x + (image_width/3)):
                move.left(60)
                print("Turning left")
            elif ball_location[1] < (center_image_x - (image_width/3)):
                move.right(60)
                print("Turning right")
            else:
                move.forward(60)
                print("forward1")
        elif (ball_location[0] < minimum_area):
            move.stop()
            print("stop2")
        else:
            move.stop()
            print("stop")
    else:
        move.stop()
        print("stop")
#let’s show the result in the output  window  
    cv2.imshow("mask",color_mask)
    cv2.imshow("frame",image) 
#always clear the stream in preparation for the next frame by calling truncate(0) between captures.
   # rawCapture.truncate(0)
    key = cv2.waitKey(1)
    if key == ord("q"):
      break
#except:
 #  pass

if __name__ == "__main__":
        try:
    #
              cam()
    #   if cv2.waitKey(1) :
    #       break
        except:
              cv2.destroyAllWindows()
              vs.stop()
    #   move.stop()


