from microbit import *

all_on = Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

def light_level():
    low_pin = pin7
    high_pin = pin3 # col 3 because it has analog in
    display.show(all_on) # light the leds
    display.off()
    low_pin.write_digital(0)
    high_pin.write_digital(1)
    v0 = high_pin.read_analog()
    sleep(1)
    v1 = high_pin.read_analog()
    display.on()
    print(v1 - v0)

while True:
    light_level()
    sleep(500)