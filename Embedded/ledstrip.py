
import board
import neopixel
size = int(input("enter number of LEDs "))
pixels = neopixel.NeoPixel(board.D18, size) #change 30 to whatever number of leds
#pixels[0] = (255, 0, 0)
address = input("want to keep changing led colors? y or n")
while address != "n":
    start = int(input("enter start of range of leds address "))
    end = int(input("enter end of range of leds tou want to address"))
    color = input("what color are these leds? (none, indianred, silver, aqua, mediumpurple, orange, red, yellow, springgreen, cornflowerblue): ")

    if color == "none":
        rgb_color = (0, 0, 0)
    elif color == "indianred":
        rgb_color = (205, 92, 92)
    elif color == "silver":
        rgb_color = (192, 192, 192)
    elif color == "aqua":
        rgb_color = (0, 255, 255)
    elif color == "mediumpurple":
        rgb_color = (147, 112, 219)
    elif color == "orange":
        rgb_color = (255, 165, 0)
    elif color == "red":
        rgb_color = (255, 0, 0)
    elif color == "yellow":
        rgb_color = (255, 255, 0)
    elif color == "springgreen":
        rgb_color = (0, 255, 127)
    elif color == "cornflowerblue":
        rgb_color = (100, 149, 237)
    else:
        print("Invalid color")
        continue
    for i in range(start, end+1):
        pixels[i] = rgb_color
    address = input("Want to keep changing LED colors? (y or n): ")
