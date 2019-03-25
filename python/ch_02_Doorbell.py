from microbit import *
import music

while True:
    if button_a.was_pressed():
        music.play(music.ENTERTAINER)
    elif button_b.was_pressed():
        music.play(music.FUNERAL)