import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
import time








GPIO.output(4, 1)

time.sleep(0.2)
GPIO.output(4, 0)

time.sleep(0.2)


GPIO.output(4, 1)

time.sleep(0.2)
GPIO.output(4, 0)

time.sleep(0.2)



GPIO.output(4, 1)

time.sleep(0.2)
GPIO.output(4, 0)

time.sleep(0.2)





GPIO.output(4, 1)

time.sleep(0.2)
GPIO.output(4, 0)



time.sleep(1) # delays for 5 seconds


GPIO.output(4, 1)


#import time
time.sleep(0.2) # delays for 5 seconds


GPIO.output(4, 0)

time.sleep(0.2)


GPIO.output(4, 1)


#import time
time.sleep(0.2) # delays for 5 seconds


GPIO.output(4, 0)


