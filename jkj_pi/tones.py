import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO_PIN = 21

GPIO.setup(GPIO_PIN, GPIO.OUT)

pwm = GPIO.PWM (GPIO_PIN, 500)

pwm.start(50)

try:

	while True:

		Freq = input("Please input a new frequency (50-5000):")
		Frequency = int(Freq)
		pwm.ChangeFrequency(Frequency)



except:
	GPIO.cleanup()


