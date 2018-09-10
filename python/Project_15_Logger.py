from microbit import *
from math import log
import os

sample_period = 60000
filename = 'data.txt'
temp_pin = pin1
light_pin = pin2

last_sample_time = 0
recording = False
display.show(Image.NO)

def read_c():
    r0 = 100000.0
    r2 = 100000.0
    b = 4250.0
    v33 = 3.3 # actually result is independent of this value
    V = temp_pin.read_analog() * v33 / 1023.0
    R = r2 * (v33 - V) / V
    t0 = 273.15     # 0 deg C in K
    t25 = t0 + 25.0 # 25 deg C in K
    # Steinhart-Hart equation - Google it
    inv_T = 1/t25 + 1/b * log(R/r0)
    T = (1/inv_T - t0)
    return round(T, 1)
    
def read_f(self):
    return read_c() * 9/5 + 32

while True:
    if button_a.was_pressed():
        recording = not recording
        if recording:
            display.show(".")
            try: 
                os.remove(filename)
            except:
                pass
            fs = open(filename, 'w')
        else:
            display.show(Image.NO)
            fs.close()
    now = running_time()
    if now > last_sample_time + sample_period:
        last_sample_time = now
        if recording:
            temp = read_c()
            light = light_pin.read_analog()
            fs.write(str(temp) + "," + str(light))
            fs.write('\n')
            