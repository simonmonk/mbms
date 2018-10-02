from microbit import *

def sound_level():
    # find max of 10 readings
    max_level = 0
    for i in range(0, 10):
        level = (pin0.read_analog() - 511) / 100
        if level > max_level:
            max_level = level
    return max_level

def bargraph(a):
    display.clear()
    for y in range(0, 5):
        if a > y:
            for x in range(0, 5):
                display.set_pixel(x, 4-y, 9)
                
while True:
    bargraph(sound_level())
    sleep(10)