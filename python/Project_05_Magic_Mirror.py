from microbit import *
import neopixel, random

leds = neopixel.NeoPixel(pin0, 30)

while True:
    led = random.randint(0, 29)
    if random.randint(0, 3) == 0:
        leds[led] = (127, 127, 0)
    else:
        leds[led] = (0, 0, 0)
    leds.show()
    sleep(5)