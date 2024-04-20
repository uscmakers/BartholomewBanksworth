#######################################
# Copyright (c) 2021 Maker Portal LLC
# Author: Joshua Hrisko
#######################################
#
# NEMA 17 (17HS4023) Raspberry Pi Tests
# --- rotating the NEMA 17 to test
# --- wiring and motor functionality
#
#
#######################################
#
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

################################
# RPi and Motor Pre-allocations
################################
#
#define GPIO pins
direction= 26 # Direction (DIR) GPIO Pin
step = 20 # Step GPIO Pin
EN_pin = 21 # enable pin (LOW to enable)

magnet = 17

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

###########################
# Actual motor control
###########################
#
# 0.002 step delay is good when the lever is not attached
while True:
    command = input("What step delay do you want to use? 0.0005 is the default. -1 to quit.")
    if command == "-1":
        break
    elif command == "0":
        GPIO.output(EN_pin, GPIO.HIGH)
    else:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output
        GPIO.setup(magnet,GPIO.OUT) # set enable pin as output
        GPIO.output(magnet, GPIO.LOW)
        GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
        mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                            200, # number of steps
                            float(command), # step delay [sec]
                            False, # True = print verbose output 
                            .05) # initial delay [sec]
        GPIO.output(magnet, GPIO.HIGH)
        GPIO.cleanup() # clear GPIO allocations after run

GPIO.output(EN_pin, GPIO.HIGH)
GPIO.cleanup() # clear GPIO allocations after run