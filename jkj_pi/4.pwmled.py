import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False)

pin =21

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin,GPIO.OUT)

pwm_led =GPIO.PWM(pin,50)

pwm_led.start(100)

try:

	while True:

		duty_s= input("Enter Brightness  Value(0 to 100):")

		duty=int(duty_s)

		pwm_led.ChangeDutyCycle(duty)

		time.sleep(0.5)



except:

	GPIO.cleanup()




