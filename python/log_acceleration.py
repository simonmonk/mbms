from microbit import *
from math import sqrt

while True:
    x, y, z = accelerometer.get_values()
    net = sqrt(x*x + y*y + z*z)
    print((net,))
    sleep(100)