import machine, neopixel, random

leds = neopixel.NeoPixel(machine.Pin(0), 30)

while True:
    led = random.randint(0, 29)
    if random.randint(0, 3):
        leds[0] = (127, 127, 0)
    else:
        leds[0] = (0, 0, 0)
    time.sleep(5)