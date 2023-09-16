#blink an LED light
#concept: blending

import time
import board

from rainbowio import colorwheel

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.05

# PHASE 1: changing between RGB (very original)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
#a time counter counts the strating time
#and if it is on for 10 sec changing between rgb
#then move on
startTime = time.monotonic()
while time.monotonic() - startTime < 10:
    led.brightness = 0.05
    led.fill(red)
    time.sleep(0.5)
    led.fill(green)
    time.sleep(0.5)
    led.fill(blue)
    time.sleep(0.5)


# Phase 2: changing between the colorwheel (starts blending)
#a time counter counts the strating time
#and if it is on for 10 sec changing between colorwheel
#then move on
startTime = time.monotonic()
while time.monotonic() - startTime < 15:
    led.brightness = 0.5
    #picking the color using changing i
    i = (time.monotonic() - startTime) / 10 * 255
    led.fill(colorwheel(int(i)))
    time.sleep(0.01)

    #Question: how can i store the variable i value at the end of the execution of while loop
    #and gradually add it up to 255,255,255


# Phase 3: Gradually transition to white and stay white (rgb blending completely)
white = (255, 255, 255)
#a time counter counts the strating time
#and if it is on for 10 sec being white
#ends
startTime = time.monotonic()
while time.monotonic() - startTime < 5:
    led.fill(white)
    led.brightness = 0.5
    time.sleep(1)
