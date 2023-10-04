# neo
import digitalio
import board
from rainbowio import colorwheel
import neopixel
import random

# photocell
import time
from analogio import AnalogIn

# mp3
import board
import busio
import audioio
import audiomp3
import adafruit_lis3dh

# photocell
potentiometer = AnalogIn(board.A1)  # Potentiometer connected to A1, power & ground

darkThreshold = 9000
brightThreshold = 20000

# NeoPixel
NUM_PIXELS = 9  # NeoPixel ring length (in pixels)
BRIGHTNESS = 0.1
strip = neopixel.NeoPixel(board.D5, NUM_PIXELS, brightness=BRIGHTNESS)

# MP3
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True
speaker = audioio.AudioOut(board.A0)
sample_number = 0
samples = ["happy.mp3", "slow.mp3"]

interval = 0.6  # Time in seconds for color change
last_time = time.monotonic()

while True:
    brightness = potentiometer.value

    if brightness > brightThreshold:
        print("bright")
        # Turn off NeoPixels
        strip.fill((0, 0, 0))
        strip.show()
        if speaker.playing is True:
            speaker.stop()
            time.sleep(0.1)
    elif brightness < darkThreshold:
        print("dark")
        if speaker.playing is False:
            sample = samples[sample_number]
            print("Now playing: '{}'".format(sample))
            mp3stream = audiomp3.MP3Decoder(open(sample, "rb"))
            speaker.play(mp3stream)
            sample_number = (sample_number + 1) % len(samples)

        current_time = time.monotonic()
        if current_time - last_time >=interval:
            for i in range(NUM_PIXELS):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                strip[i] = (r, g, b)
            strip.show()
            last_color_change_time = current_time

    time.sleep(0.25)
