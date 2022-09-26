import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
trigger =12
echo = 25
pin =21
GPIO.setup(trigger , GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(pin,GPIO.OUT)
def distance():
	GPIO.output(trigger, False)
	time.sleep(0.000001)
	GPIO.output(trigger, True)
	time.sleep(0.000001)
	GPIO.output(trigger, False)
	time.sleep(0.000001)
	while GPIO.input(echo) == 0:
		Pulse_StartTime = time.time()
	while GPIO.input(echo) == 1:
		Pulse_StopTime = time.time()
	Pulse_duration = Pulse_StopTime - Pulse_StartTime
	distance = (Pulse_duration * 34300)/2
	return distance
if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			time.sleep(0.1)
			print("Distance is : " , dist, "cm" )
			if dist< 20:
				print ("led & buzzer  off")
				GPIO.output(pin,False)
			else:
				print ("led & buzzer  on")
				GPIO.output(pin,True)

	except:
		print("Measurement stopped ")
		GPIO.cleanup()
