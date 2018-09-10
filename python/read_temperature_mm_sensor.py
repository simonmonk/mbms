from microbit import *
from math import log

temp_pin = pin0

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
    return T
    
def read_f(self):
    return read_c() * 9/5 + 32
    
while True:
    print(read_c())
    sleep(1000)