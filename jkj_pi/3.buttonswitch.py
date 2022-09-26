import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

switch = 16

pin = 21

GPIO.setup(switch, GPIO.IN)

GPIO.setup(pin, GPIO.OUT)

try:

    while True:

         button_state = GPIO.input(switch)

         if button_state == False:

             GPIO.output(pin, False)

             print ('Button not Pressed...')

             time.sleep(0.2)

         else:

             GPIO.output(pin, True)

             print ('Button pressed')

except:

    GPIO.cleanup()


