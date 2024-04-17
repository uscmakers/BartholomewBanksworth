import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D23, 30)

for x in range(0, 9):
    pixels[x] = (255, 0, 0)
    time.sleep(1)