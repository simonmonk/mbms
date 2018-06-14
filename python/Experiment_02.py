from microbit import *
import speech

while True:
    if button_a.was_pressed():
        speech.say("Mad Scientists love micro bits")