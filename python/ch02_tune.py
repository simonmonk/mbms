from microbit import *
import music

notes = ['A4:4', 'A', 'A', 'F:2', 'C5:2', 'A4:4', 'F:2', 'C5:2', 'A4:4']

while True:
    if button_a.was_pressed():
        music.play(notes)