
import board
import neopixel
size = input("enter number of LEDs")
pixels = neopixel.NeoPixel(board.D18, size) #change 30 to whatever number of leds
pixels[0] = (255, 0, 0)