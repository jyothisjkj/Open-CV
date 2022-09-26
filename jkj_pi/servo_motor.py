import RPi.GPIO as GPIO  

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

servo=18

GPIO.setup(servo,GPIO.OUT)

i=GPIO.PWM(servo,50) 

i.start(2.5)

def servo():

	while True:

		i.ChangeDutyCycle(2.5)

		print("0 degree")

		time.sleep(1)

		i.ChangeDutyCycle(7.5)

		print("90 degree")

		time.sleep(1)

		i.ChangeDutyCycle(12.5)

		print("180 degree")

		time.sleep(1)

if __name__=='__main__':

	try:

		servo()



	except:

		GPIO.cleanup()


