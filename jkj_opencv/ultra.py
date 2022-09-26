import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 12
GPIO_ECHO = 25

GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)
#print ("Waiting For Sensor To Settle")
#time.sleep(2)
def Distance():
#	while True:
        #trigger the ultrasonic sensor for a very short period (10us).
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
        
	while GPIO.input(GPIO_ECHO) == 0:
		pass
	StartTime = time.time() #start timer once the pulse is sent completely and echo becomes high or 1
	while GPIO.input(GPIO_ECHO) == 1:
		pass
	StopTime = time.time() #stop the timer once the signal is completely received  and echo again becomes 0
	TimeElapsed = StopTime - StartTime # This records the time duration for which echo pin was high 
	speed=34300 #speed of sound in air 343 m/s  or 34300cm/s
	twicedistance = (TimeElapsed * speed) #as time elapsed accounts for amount of time it takes for the pulse to go and come back  
	distance=twicedistance/2  # to get actual distance simply divide it by 2
	time.sleep(.01)
	
	dis= round(distance,2) # round off upto 2 decimal points
	print (dis)
	return dis

