import time 
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import ultra
import move
font = cv2.FONT_HERSHEY_SIMPLEX 
# Are we using the Pi Camera?
usingPiCamera = True
# Set initial frame size.
frameSize = (320, 240)
 
# Initialize mutithreading the video stream.
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
        framerate=32).start()
# Allow the camera to warm up.
time.sleep(2.0)
 
#timeCheck = time.time()
def checkforred(image):
    font = cv2.FONT_HERSHEY_SIMPLEX
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        #Red HSV Range
    low_red=np.array([157,56,0])
    high_red=np.array([179,255,255])
    mask=cv2.inRange(hsv,low_red,high_red)
    blur=cv2.GaussianBlur(mask,(15,15),0)
    _ ,contours, hierarchy=cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    status=0
    for contour in contours:
        area=cv2.contourArea(contour)
        if area>20000:
            status=1
            cv2.drawContours(image,contour,-1,(0,0,255),3)
            cv2.putText(image,'RED STOP',(240,320), font, 2,(0,0,255),2,cv2.LINE_AA)     
        return (image,status)

def average_slope_intercept(lines,image):
        left_fit=[]
        right_fit=[]
        if lines is not None:
            for line in lines:
                x1,y1,x2,y2=line.reshape(4)
                parameters=np.polyfit((x1,x2),(y1,y2),1)
                slope=parameters[0]
                intercept=parameters[1]
                #move.forward(60)
                if slope<0:
                    right_fit.append((slope,intercept))
                    
                    
                 #   move.left(50)
                else:
                    left_fit.append((slope,intercept))
                    
                  #  move.right(50) 
        left_fitavg=np.average(left_fit, axis=0)
        right_fitavg=np.average(right_fit, axis=0)
        #print("left slope",left_fit,"rigt slope",right_fit)
        
 #       distance=ultra.Distance() #Get current Distance from US sensor
        left= len(left_fit)
        
        right = len(right_fit)
       # print("distance=",distance)
    
        print("left=",left)
        print("right=",right)
        return left,right;
    

        
       # self.sendinfoback(len(left_fit), len(right_fit),red=0) # Send number of left and right lines detected.

def canny_img(image):
        gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        blur=cv2.GaussianBlur(gray, (7,7), 0)
        canny=cv2.Canny(blur,50,150)  # lowerThreshold=50 UpperThreshold=150 
        return canny

def region_of_interest(image):
        height=image.shape[0]
        width=image.shape[1]
#         region=np.array([[(120,height),(width-120,height),(width-120,height-160),(120,height-160)]])
        region = np.array([[(0, height),(0,  height/2),(width , height/2),(width , height),]], np.int32)    
        mask=np.zeros_like(image)
        cv2.fillPoly(mask,region, 255)
        return mask
    
def display_lines(lines,image):
        line_image=np.zeros_like(image)
        if lines is not None:
            for line in lines:
                if len(line)>0:                    
                    x1,y1,x2,y2=line.reshape(4)
                    cv2.line(line_image,(x1,y1),(x2,y2),[0,255,0],10)
        return line_image
while True:
    # Get the next frame.
    frame = vs.read()
    img = cv2.flip(frame, 0)
    image = cv2.flip(img, 1)
    lane_image=np.copy(image)
   # red=checkforred(lane_image)

    #if red:
     #      checkforred()
           
   # else:
    canny=canny_img(lane_image)
    roi=region_of_interest(canny)
    lane=cv2.bitwise_and(canny,roi)
    lines=cv2.HoughLinesP(lane,1,np.pi/180,30,np.array([]),minLineLength=20,maxLineGap=5)        
    line_image=display_lines(lines,lane_image)    
    lane_image=cv2.addWeighted(lane_image,1,line_image,1,0)
    left,right = average_slope_intercept(lines,lane) 
    #line_image=display_lines(lines,lane_image)                    
    #lane_image=cv2.addWeighted(lane_image,1,line_image,1,0)
    #distance =ultra.Distance()
    #print ("distance=",distance)
    #if distance < 15: # Stop the car if condition is true 
     #   move.stop()
      #  cv2.putText(image,'stop', (5,100),font,1,(255,255,0),2)
       # print ("stop")
    if (left > right): # if left is more ==> move left by stopping the left wheel.
        move.left(left+25)
        cv2.putText(image,'left', (5,100),font,1,(255,255,0),2)
        print ("left")
    elif(right > left): # if right is more==> move right by stopping the right wheel.
        move.right(right+25)
        cv2.putText(image,'right', (5,100),font,1,(255,255,0),2)
        print ("right")
    #elif(right==0 and left==0):
     #   move.stop()
    else:
        move.forward(60)
        cv2.putText(image,'forward', (5,100),font,1,(255,255,0),2)
        print ("frd")        
    
        
    cv2.imshow('canny',canny)
    cv2.imshow('roi',roi)
    cv2.imshow('lane',lane)
    cv2.imshow('line',line_image)
    cv2.imshow('frame',lane_image)
    cv2.imshow('orig', image)
    key = cv2.waitKey(1) & 0xFF
    #rawCapture.truncate(0) 
    # if the `q` key was pressed, break from the loop.
    if key == ord("q"):
        break
    
    #print(1/(time.time() - timeCheck))
    #timeCheck = time.time()

cv2.destroyAllWindows()
vs.stop()
move.stop()

