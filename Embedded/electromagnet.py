
from gpiozero import OutputDevice
import time

# Define the GPIO pin connected to the electromagnet
electromagnet = OutputDevice(17)  # Change 17 to the actual GPIO pin number you're using

try:
    while True:
        # Turn the electromagnet on
        electromagnet.on()
        print("Electromagnet is ON")
        time.sleep(2)  # Keep it on for 2 seconds
        
        # Turn the electromagnet off
        electromagnet.off()
        print("Electromagnet is OFF")
        time.sleep(2)  # Keep it off for 2 seconds

except KeyboardInterrupt:
    # If you press Ctrl+C, exit the loop and clean up GPIO
    electromagnet.off()
    print("Exiting the program")
