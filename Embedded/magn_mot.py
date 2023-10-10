import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

################################
# RPi and Motor Pre-allocations
################################
#
#define GPIO pins
direction= 22 # Direction (DIR) GPIO Pin
step = 23 # Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

###########################
# Actual motor control
###########################
#
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor

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
    mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     50, # number of steps
                     .0105, # step delay [sec]
                     False, # True = print verbose output 
                     .05) # initial delay [sec]
    GPIO.output(magnet, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(magnet, GPIO.LOW)
     mymotortest.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                    "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                    50, # number of steps
                    .0105, # step delay [sec]
                    False, # True = print verbose output 
                    .05) 
    time.sleep(5)



    pass

GPIO.cleanup() # clear GPIO allocations after run