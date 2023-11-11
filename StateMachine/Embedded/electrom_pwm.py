import RPi.GPIO as GPIO
import time
"""
#hardware pwm example:
from rpi_hardware_pwm import HardwarePWM

pwm = HardwarePWM(pwm_channel=0, hz=60)
pwm.start(100) # full duty cycle

pwm.change_duty_cycle(50)
pwm.change_frequency(25_000)

pwm.stop()
"""
# easier way than just writing the same code four times
# Set the GPIO pin for your electromagnetic module
#these are the hardware pwm pins but the software pwm can be used on any gpio pins (we are using software pwm)

mag_pin1 = 12
mag_pin2 = 13
mag_pin3 = 18
mag_pin4 = 19




# Initialize GPIO settings
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mag_pin1, GPIO.OUT)
GPIO.setup(mag_pin2, GPIO.OUT)
GPIO.setup(mag_pin3, GPIO.OUT)
GPIO.setup(mag_pin4, GPIO.OUT)

freq = int(input("what frequency (1000 for example):))
duty = int(input("what duty cycle % is it on (0-100):))
t = int(input("how long to sleep for:)

# Initialize PWM on the mag_pin1
pwm1 = GPIO.PWM(mag_pin1, freq)  # 1000 Hz frequency
pwm2 = GPIO.PWM(mag_pin2, freq)  
pwm3 = GPIO.PWM(mag_pin3, freq)  
pwm4 = GPIO.PWM(mag_pin4, freq)  


pwm1.start(0)  # Starts with 0% duty cycle
pwm1.ChangeDutyCycle(duty) # pwm to 101


pwm2.start(0)
pwm2.ChangeDutyCycle(duty)


pwm3.start(0)
pwm3.ChangeDutyCycle(duty)


pwm4.start(0)
pwm4.ChangeDutyCycle(duty)


q = 1
while q:
  pwm1.ChangeDutyCycle(duty)
  pwm2.ChangeDutyCycle(duty)
  pwm3.ChangeDutyCycle(duty)
  pwm4.ChangeDutyCycle(duty)
  freq = int(input("what frequency (1000 for example):))
  duty = int(input("what duty cycle % is it on (0-100):))
  q = int(input("want to quit? (0 to quit, 1 to stay): )
  t = int(input("how long to sleep for:)
  time.sleep(t)


pwm1.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()


  
