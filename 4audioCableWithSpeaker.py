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

touch_pad1 = board.A1
touch1 = touchio.TouchIn(touch_pad1)

touch_pad2 = board.A2
touch2 = touchio.TouchIn(touch_pad2)

touch_pad5 = board.A5
touch5 = touchio.TouchIn(touch_pad5)

touch_pad4 = board.A4
touch4 = touchio.TouchIn(touch_pad4)


while True:
    value_A1 = touch1.raw_value
    print(value_A1)
    if doubletap == True:
        for i in range(0, 24):
            pixels[i] = (150, 67, 33)
            pixels.show()
    elif touch1.value:
        #ßtap = tap + 1
        for i in range(0, 6):
            pixels[i] = (200, 55, 104)
            pixels.show()
        #tap = tap + 1
    else:
        for i in range(0, 6):
            pixels[i] = (0, 0, 0)
            pixels.show()

    value_A2 = touch2.raw_value
    #print(value_A2)
    if doubletap == True:
        for i in range(0, 24):
            pixels[i] = (150, 67, 33)
            pixels.show()
    elif touch2.value:
        for i in range(6, 12):
            pixels[i] = (255, 0, 0)
            pixels.show()
    else:
        for i in range(6, 12):
            pixels[i] = (0, 0, 0)
            pixels.show()

    if doubletap == True:
        for i in range(0, 24):
            pixels[i] = (150, 67, 33)
            pixels.show()
    elif touch5.value:
        for i in range(12, 18):
            pixels[i] = (100,150,20)
            pixels.show()
    else:
        for i in range(12, 18):
            pixels[i] = (0, 0, 0)
            pixels.show()

    if doubletap == True:
        for i in range(0, 24):
            pixels[i] = (150, 67, 33)
            pixels.show()
    elif touch4.value:
        for i in range(18, 24):
            pixels[i] = (0, 255, 255)
            pixels.show()
    else:
        for i in range(18, 24):
            pixels[i] = (0, 0, 0)
            pixels.show()


    if (touch4.value or touch5.value) and (touch1.value or touch2.value):
        doubletap = True
    else:
        doubletap= False



    if tap == 1:
        print("Now playing: '{}'".format("bgm.mp3"))
        mp3stream = audiomp3.MP3Decoder(open("bgm.mp3", "rb"))
        speaker.play(mp3stream)
        enable.value = speaker.playing



