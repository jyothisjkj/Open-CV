import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

TRIGGER =12

ECHO =25

in1=5

in2=6

in3=27

in4=17

ena =19

enb =26

GPIO.setup(TRIGGER, GPIO.OUT)

GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(in1, GPIO.OUT)

GPIO.setup(in2, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT) 

GPIO.setup(in4, GPIO.OUT)

GPIO.setup(ena, GPIO.OUT) 

GPIO.setup(enb, GPIO.OUT) 

speed=60

p = GPIO.PWM(ena, 1000)

i= GPIO.PWM(enb, 1000)

p.start(speed)

i.start(speed)

def forward():

	GPIO.output(in1,GPIO.HIGH)

	GPIO.output(in2,GPIO.LOW)

	GPIO.output(in3,GPIO.HIGH)

	GPIO.output(in4,GPIO.LOW)

	p.ChangeDutyCycle(speed)

	i.ChangeDutyCycle(speed)

def backward():

	GPIO.output(in1,GPIO.LOW)

	GPIO.output(in2,GPIO.HIGH)

	GPIO.output(in3,GPIO.LOW)

	GPIO.output(in4,GPIO.HIGH)

	p.ChangeDutyCycle(speed)

	i.ChangeDutyCycle(speed)

def right():

	GPIO.output(in1,GPIO.HIGH)

	GPIO.output(in2,GPIO.LOW)

	GPIO.output(in3,GPIO.LOW)

	GPIO.output(in4,GPIO.HIGH)

	p.ChangeDutyCycle(speed)

	i.ChangeDutyCycle(speed)

def stop():

        GPIO.output(in1,GPIO.LOW)

        GPIO.output(in2,GPIO.LOW)

        GPIO.output(in3,GPIO.LOW)

        GPIO.output(in4,GPIO.LOW)

def distance():

	GPIO.output(TRIGGER, False)

	time.sleep(0.00001)

	GPIO.output(TRIGGER, True)

	time.sleep(0.00001)



	GPIO.output(TRIGGER, False)



	while GPIO.input(ECHO) == 0:

		Pulse_StartTime = time.time()

	while GPIO.input(ECHO) == 1:

		Pulse_StopTime = time.time()

	Pulse_duration = Pulse_StopTime - Pulse_StartTime

	distance = (Pulse_duration * 34300) / 2

	return distance

def code():

	while True:

		dist = distance()

		print ("Measured Distance is:", dist, "cm")

		time.sleep(0.25)

		if  dist <25:

			stop()

			print ("stop")

			time.sleep(0.3)

			backward()

			print ("backward")

			time.sleep(0.5)

			right()

			print ("right")

			time.sleep(0.7)

		else:

			forward() 

			print ("frd")

if __name__=='__main__':

	try:

		code()

	except:

		GPIO.cleanup()


