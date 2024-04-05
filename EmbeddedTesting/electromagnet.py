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
while True:
    GPIO.output(magnet, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(magnet, GPIO.LOW)
    time.sleep(5)

GPIO.cleanup() # clear GPIO allocations after run