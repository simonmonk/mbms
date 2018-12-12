from microbit import *

while True:
    heading = compass.heading()
    if heading > 10 and heading < 180:
        display.show(Image.ARROW_W)
    elif heading >= 180 and heading < 350:
        display.show(Image.ARROW_E)
    else:
        display.show(Image.ARROW_N)
        
    if button_a.was_pressed():
        compass.calibrate()
        