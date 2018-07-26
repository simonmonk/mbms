from microbit import *
from math import sqrt
import os

filename = 'data.txt'

recording = False
display.show(Image.NO)

while True:
    if button_a.was_pressed():
        recording = not recording
        if recording:
            display.show(Image.YES)
            try: 
                os.remove(filename)
            except:
                pass
            fs = open(filename, 'w')
        else:
            display.show(Image.NO)
            fs.close()
    if recording:
        a = accelerometer.get_values()
        net = sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
        fs.write(str(net))
        fs.write('\n')
        sleep(10)