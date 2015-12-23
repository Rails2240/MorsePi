print "Hello, Python!"

import RPi.GPIO as GPIO

#The following is test code for the GPIO

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)

