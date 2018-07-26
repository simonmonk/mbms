from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.HAPPY)
        sleep(500)
        display.clear()