# Write your code here :-)
# Write your code here :-)
import time
import board
import touchio

import digitalio
from rainbowio import colorwheel
import neopixel

import busio
import digitalio
import audioio
import audiomp3
import adafruit_lis3dh

NUM_PIXELS = 24  # NeoPixel ring length (in pixels)
BRIGHTNESS = 1  # Let's not blind everyone

tap = 0
doubletap = False

startup_play = False  # set to True to play all samples once on startup

# Set up accelerometer on I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D6)
accel = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
accel.set_tap(1, 100)  # single or double-tap, threshold

# Set up speaker enable pin
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True

speaker = audioio.AudioOut(board.A0)

sample_number = 0
samples = ['bgm.mp3']

#Play = [0,0,0,0]

# The power for the NeoPixels is not enabled by default (to save battery power)
# We need to turn on the power by setting pin D10 high
print("Enabling NeoPixel power!")
enable2 = digitalio.DigitalInOut(board.D11)
enable2.direction = digitalio.Direction.OUTPUT
enable2.value = True

print("hello")
pixels = neopixel.NeoPixel(board.D5, NUM_PIXELS, brightness=0.5, auto_write=False)

#strip = neopixel.NeoPixel(board.D5, NUM_PIXELS, brightness=BRIGHTNESS)

touch_pad2 = board.A2
touch2 = touchio.TouchIn(touch_pad2)


touch_pad4 = board.A4
touch4 = touchio.TouchIn(touch_pad4)


while True:
#middle1
    value_A2 = touch2.raw_value
    #print(value_A2)
    if doubletap == True:
        for i in range(0, 24):
            pixels[i] = (255, 150, 0)
            pixels.show()
    elif touch2.value:
        for i in range(0, 12):
            pixels[i] = (230, 50, 150)
            pixels.show()
    else:
        for i in range(0, 12):
            pixels[i] = (0, 0, 0)
            pixels.show()

#middle 2
    value_A4 = touch4.raw_value
    #print(value_A4)
    if doubletap == True:
        for i in range(0, 24):
            pixels[i] = (255, 150, 0)
            pixels.show()
    elif touch4.value:
        for i in range(12, 24):
            pixels[i] = (50, 150, 255)
            pixels.show()
    else:
        for i in range(12, 24):
            pixels[i] = (0, 0, 0)
            pixels.show()


    if touch4.value and touch2.value:
       # print("gs")
        doubletap = True
    else:
        doubletap= False


