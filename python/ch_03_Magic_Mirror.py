from microbit import *
import neopixel, random

leds = neopixel.NeoPixel(pin0, 30)

while True:
    led = random.randint(0, 29)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    leds[led] = color
    leds.show()
    sleep(5)