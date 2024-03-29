import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

try :
	while True:
		if GPIO.input(25) == True:
			print("Sensor ON!!")
			GPIO.output(16, True)
			time.sleep(0.2)
		if GPIO.input(25) == False:
			print("Sensor OFF!!")
			GPIO.output(16, False)

except KeyboardInterrupt:
	GPIO.cleanup()
