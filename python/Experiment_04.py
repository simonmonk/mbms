from microbit import *

while True:
    display.scroll(str(int(compass.get_field_strength() / 1300)))