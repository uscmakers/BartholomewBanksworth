import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)

for x in range(0, 9):
    pixels[x] = (255, 0, 0)
    sleep(1)