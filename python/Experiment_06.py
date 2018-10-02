from microbit import *
from math import sqrt

while True:
    x, y, z = accelerometer.get_values()
    net = sqrt(x*x + y*y + z*z)
    all = (x, y, z, net)
    print(all)
    sleep(100)
        
        
        
        23 16.5 2
        
        