import RPi.GPIO  as  GPIO    #Libraries

import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

in1=5  #set 6 pin to in1

in2=6  #set 5 pin to in2

in3=27   #set 27 pin to in3

in4=17 #set 17 pin to in4

ena=19

enb=26

GPIO.setup(in1, GPIO.OUT)  #set in1 to be an output

GPIO.setup(in2, GPIO.OUT) #set in2  to be an output

GPIO.setup(in3, GPIO.OUT)   #set in3  to be an output 

GPIO.setup(in4, GPIO.OUT)   #set in4  to be an output

GPIO.setup(ena, GPIO.OUT)  #set ena to be  an output,enable pin is use to control the speed of motor

GPIO.setup(enb, GPIO.OUT)



p=GPIO.PWM(ena,1000)  #50hz frequency

i=GPIO.PWM(enb,1000)  #50hz frequency

p.start(0) #start duty cycle

i.start(0) #start duty cycle

def forward(speed):   #motor rotate in forward direction

    GPIO.output(in1,GPIO.LOW)

    GPIO.output(in2,GPIO.HIGH)

    GPIO.output(in3,GPIO.LOW)

    GPIO.output(in4,GPIO.HIGH)

    p.ChangeDutyCycle(speed)

    i.ChangeDutyCycle(speed)

def reverse(turn_speed):     #motor rotate in reverse direction

    GPIO.output(in1,GPIO.HIGH)

    GPIO.output(in2,GPIO.LOW)

    GPIO.output(in3,GPIO.HIGH)

    GPIO.output(in4,GPIO.LOW)

    p.ChangeDutyCycle(turn_speed)

    i.ChangeDutyCycle(turn_speed)

def right(turn_speed):     #motor rotate in right direction

    GPIO.output(in1,GPIO.LOW)

    GPIO.output(in2,GPIO.HIGH)

    GPIO.output(in3,GPIO.HIGH)

    GPIO.output(in4,GPIO.LOW)

    p.ChangeDutyCycle(turn_speed)

    i.ChangeDutyCycle(turn_speed)



def left(turn_speed):     #motor rotate in left direction

    GPIO.output(in1,GPIO.HIGH)

    GPIO.output(in2,GPIO.LOW)

    GPIO.output(in3,GPIO.LOW)

    GPIO.output(in4,GPIO.HIGH)

    p.ChangeDutyCycle(turn_speed)

    i.ChangeDutyCycle(turn_speed)



def stop():     #motor stop

    GPIO.output(in1,GPIO.LOW)

    GPIO.output(in2,GPIO.LOW)

    GPIO.output(in3,GPIO.LOW)

    GPIO.output(in4,GPIO.LOW)

    p.ChangeDutyCycle(0)

    i.ChangeDutyCycle(0)

def code ():

	while True:

		forward (80)

		print("forward")

		time.sleep(0.5)

		stop ()

		print("stop")

		time.sleep(1)

		reverse(80)

		print("reverse")

		time.sleep(0.5)

		stop ()

		print("stop")

		time.sleep(1)

		left (80)

		print("left")

		time.sleep(1)

		stop ()

		print("stop")

		time.sleep(1)

		right (80)

		print("right")

		time.sleep(1)

		stop ()

		print("stop")

		time.sleep(1)



if __name__=='__main__':

	try:

		code ()

	except:

		GPIO.cleanup()


