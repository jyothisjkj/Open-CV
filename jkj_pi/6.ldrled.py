import RPi.GPIO as GPIO 

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False) 

ldr=4

pin=21

GPIO.setup(pin,GPIO.OUT)

try:

	while True:

		GPIO.setup(ldr,GPIO.OUT)

		GPIO.output(ldr,GPIO.LOW)

		time.sleep(0.1)

		time_diff =0

		GPIO.setup(ldr,GPIO.IN)

		currenttime=time.time()

		while(GPIO.input(ldr)==GPIO.LOW):

			time_diff=time.time()-currenttime  

		value=time_diff*1000

		print (value)

		time.sleep(0.2)

		if value< 2:

			print ("led & buzzer  off") 

			GPIO.output(pin,False)

		else:

			print ("led & buzzer  on")

			GPIO.output(pin,True)

except:

	GPIO.cleanup()


