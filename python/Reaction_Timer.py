from microbit import *
from random import randint


while True:
    if button_a.was_pressed():
        start_time = 0
        display.show(Image.SQUARE)
        delay = randint(3000, 6000)
        sleep(delay)
        display.clear()
        start_time = running_time()
    if button_b.was_pressed():
        end_time = running_time()
        reaction_time = end_time - start_time
        if reaction_time == 0:
            display.show(Image.NO)
        else:
            display.scroll(str(reaction_time))