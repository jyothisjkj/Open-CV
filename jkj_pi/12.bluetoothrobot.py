from bluedot import  BlueDot

import RPi.GPIO  as  GPIO

from signal import pause

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

bd=BlueDot()

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

speed=100

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

def move(pos):

	if pos.top:

		forward()

		print("forward")

	elif pos.bottom:

		backward()

		print("backward")

	elif pos.left:

		left()

		print("left")

	elif pos.right:

		right()

		print("right")

	else:

		stop()
		print("stop")
		
bd.when_pressed=move

bd.when_moved=move

bd.when_released=stop

pause()


