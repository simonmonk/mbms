from microbit import *
from math import sqrt

while True:
    x, y, z = accelerometer.get_values()
    acc = sqrt(x*x + y*y + z*z)
    y = int(2 + (acc - 1000) / 100)
    display.clear()
    if y < 0:
        y = 0
    if y > 4:
        y = 4
    for x in range(0, 5):
        display.set_pixel(x, y, 9)