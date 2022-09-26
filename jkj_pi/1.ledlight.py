import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False) #ignore warnings

GPIO.setmode(GPIO.BCM)

pin=21

GPIO.setup(pin,GPIO.OUT)

GPIO.output(pin,GPIO.HIGH)

print ("LED&buzzer on")

time.sleep(1)

GPIO.output(pin,GPIO.LOW) 

time.sleep(1)


