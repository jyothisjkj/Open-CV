import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

pin= 21

GPIO.setup(pin, GPIO.OUT)

try:

        while True:

                GPIO.output(pin, GPIO.HIGH)

                time.sleep(1)

                print ("led and buzzer on")

                GPIO.output(pin, GPIO.LOW)

                time.sleep(1)

                print ("led and buzzer off")

except:

        GPIO.cleanup()


