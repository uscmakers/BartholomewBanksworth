import RPi.GPIO as GPIO
import time

#define GPIO pins
magnet = 18 # Step GPIO Pin

# Declare a instance of class pass GPIO pins numbers and the motor type
GPIO.setmode(GPIO.BCM)
GPIO.setup(magnet,GPIO.OUT) # set enable pin as output

###########################
# Actual motor control
###########################
#
GPIO.output(magnet, GPIO.HIGH)
while True:
    pass

GPIO.cleanup() # clear GPIO allocations after run