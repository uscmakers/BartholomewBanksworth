import RPi.GPIO as GPIO
import time

# Set the GPIO pin for your electromagnetic module
EMAG_PIN = 17

# Initialize GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(EMAG_PIN, GPIO.OUT)

# Initialize PWM on the EMAG_PIN
pwm = GPIO.PWM(EMAG_PIN, 1000)  # 1000 Hz frequency


pwm.start(0)  # Starts with 0% duty cycle
while True:
    # Increase duty cycle to strengthen the magnetic field
    for duty_cycle in range(0, 101):
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)

    # Decrease duty cycle to weaken the magnetic field
    for duty_cycle in range(100, -1, -1):
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
