import RPi.GPIO as GPIO
import time
# easier way than just writing the same code four times
# Set the GPIO pin for your electromagnetic module
mag_pin1 = 22
mag_pin2 = 23
mag_pin3 = 24
mag_pin4 = 18

# Initialize GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(mag_pin1, GPIO.OUT)
GPIO.setup(mag_pin2, GPIO.OUT)
GPIO.setup(mag_pin3, GPIO.OUT)
GPIO.setup(mag_pin4, GPIO.OUT)

# Initialize PWM on the mag_pin1
pwm1 = GPIO.PWM(mag_pin1, 1000)  # 1000 Hz frequency
pwm2 = GPIO.PWM(mag_pin2, 1000)  
pwm3 = GPIO.PWM(mag_pin3, 1000)  
pwm4 = GPIO.PWM(mag_pin4, 1000)  


pwm1.start(0)  # Starts with 0% duty cycle
pwm1.ChangeDutyCycle(101) # pwm to 101
time.sleep(5) # delay
pwm1.ChangeDutyCycle(0) # pwm to 0

pwm2.start(0)
pwm2.ChangeDutyCycle(101)
time.sleep(5)
pwm2.ChangeDutyCycle(0)

pwm3.start(0)
pwm3.ChangeDutyCycle(101)
time.sleep(5)
pwm2.ChangeDutyCycle(0)

pwm4.start(0)
pwm4.ChangeDutyCycle(101)
time.sleep(5)
pwm2.ChangeDutyCycle(0)

