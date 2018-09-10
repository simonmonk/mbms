from microbit import *

baseline = pin2.read_analog()

while True:
    if button_a.was_pressed():
        baseline = pin2.read_analog()
    reading = pin2.read_analog()
    change = int((reading - baseline) / 10)
    if (change > 2):
        change = 2
    if (change < -2):
        change = -2
    display.clear()
    display.set_pixel(2, 2 + change, 9)