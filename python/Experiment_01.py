from microbit import *
import music

while True:
    if button_a.was_pressed():
        music.pitch(262, 1000)