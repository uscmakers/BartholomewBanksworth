import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

#define GPIO pins
direction = 26 # Direction (DIR) GPIO Pin
step = 20 # Step GPIO Pin
EN_pin = 21 # enable pin (LOW to enable)

#define GPIO pins
magnet1 = 12 #  GPIO Pin for magnet 1
magnet2 = 13 #  GPIO pin for magnet 2
magnet3 = 18 #  GPIO pin for magnet 3
magnet4 = 19 #  GPIO pin for magnet 4

#define map from player number to magent GPIO pins
magnets = [magnet1, magnet2, magnet3, magnet4]

# Declare a instance of class pass GPIO pins numbers and the motor type
GPIO.setmode(GPIO.BCM)
GPIO.setup(magnet1,GPIO.OUT) # set enable pin as output for magnet 1
GPIO.setup(magnet2,GPIO.OUT) # set enable pin as output for magnet 2

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

def turnMotor(numSteps: int, clockwise: bool):
    mymotortest.motor_go(clockwise, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     numSteps, # number of steps
                     .0005, # step delay [sec]
                     True, # True = print verbose output 
                     .05) # initial delay [sec]
    
def turnMotorFaster(numSteps: int, clockwise: bool):
    mymotortest.motor_go(clockwise, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     numSteps, # number of steps
                     .0500, # step delay [sec]
                     True, # True = print verbose output 
                     .05) # initial delay [sec]
    
def electromagnetOn(num: int):
    GPIO.output(magnets[num], GPIO.HIGH)

def electromagnetOff(num: int):
    GPIO.output(magnets[num], GPIO.LOW)

turnMotorFaster(20, True)