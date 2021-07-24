import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

try :
	a = 1
	while a < 10:
		GPIO.output(16,True)
		time.sleep(1)
		GPIO.output(16,False)
		time.sleep(1)
		a = a + 1
except KeyboardInterrupt:
	GPIO.cleanup()
