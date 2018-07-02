from microbit import *
import music

while True:
    if compass.get_field_strength() < 130000:
        music.pitch(523, 1000)