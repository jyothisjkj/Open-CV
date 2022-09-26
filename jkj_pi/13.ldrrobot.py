import RPi.GPIO as GPIO 

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

ldr1=20

ldr2=4

in1=5

in2=6

in3=27

in4=17

ena =19

enb = 26

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

def right():

	GPIO.output(in1,GPIO.HIGH)

	GPIO.output(in2,GPIO.LOW)

	GPIO.output(in3,GPIO.LOW)

	GPIO.output(in4,GPIO.HIGH)

	p.ChangeDutyCycle(speed)

	i.ChangeDutyCycle(speed)

def left():

	GPIO.output(in1,GPIO.LOW)

	GPIO.output(in2,GPIO.HIGH)

	GPIO.output(in3,GPIO.HIGH)

	GPIO.output(in4,GPIO.LOW)

	p.ChangeDutyCycle(speed)

	i.ChangeDutyCycle(speed)

def stop():

	GPIO.output(in1,GPIO.LOW)

	GPIO.output(in2,GPIO.LOW)

	GPIO.output(in3,GPIO.LOW)

	GPIO.output(in4,GPIO.LOW)

	p.ChangeDutyCycle(speed)

	i.ChangeDutyCycle(speed)

def ldr_a():

	GPIO.setup(ldr1,GPIO.OUT)

	GPIO.output(ldr1,GPIO.LOW)

	time.sleep(0.5)

	difference =0

	GPIO.setup(ldr1,GPIO.IN)

	currenttime=time.time()

	while(GPIO.input(ldr1)==GPIO.LOW):

		difference=time.time()-currenttime

		value1=difference*1000

		print ("value1 is ",value1)

		return value1



def ldr_b():

	GPIO.setup(ldr2,GPIO.OUT)

	GPIO.output(ldr2,GPIO.LOW)

	time.sleep(0.5)

	difference =0

	GPIO.setup(ldr2,GPIO.IN)

	currenttime=time.time()

	while(GPIO.input(ldr2)==GPIO.LOW):

		difference=time.time()-currenttime

		value2=difference*1000

		print("value2 is ",value2)

		return value2



def code():

	while True:

		if(ldr_a()<(0.018) and ldr_b()<(0.018)):

			forward()

			print ("forward")
			time.sleep(0.5)

		elif (ldr_a()<(0.018) and ldr_b()>(0.018)):

			right()

			print ("right")
			time.sleep(0.5)

		elif (ldr_b()<(0.018) and ldr_a()>(0.018)):

			left()

			print ("left")
			time.sleep(0.5)

		else:

			stop()

			print ("stop")
			time.sleep(0.5)



if __name__=='__main__':

	try:

		code() 

	except:

		GPIO.cleanup()


