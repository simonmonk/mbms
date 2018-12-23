from microbit import *
from math import sqrt

strokes_per_point = 50
old_mg = 0
count = 0
change_in_mg = 0
score = 0
mg = 0
display.show(str(score))

while True:
    x, y, z = accelerometer.get_values()
    mg = sqrt(x*x + y*y + z*z)
    change_in_mg = mg - old_mg
    old_mg = mg
    if change_in_mg > 800:
        count += 1
        if count > strokes_per_point:
            score += 1
            display.show(str(score))
            count = 0
            if score > 9:
                display.show(Image.HAPPY)