import RPi.GPIO as GPIO

from bluedot import BlueDot

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) 

bd=BlueDot()

pin=21

GPIO.setup(pin, GPIO.OUT)

while True:	

	bd.wait_for_press()

	print("led on")

	GPIO.output(pin,GPIO.HIGH)

	bd.wait_for_release()

	GPIO.output(pin,GPIO.LOW)

	print("led off")


