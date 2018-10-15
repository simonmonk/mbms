from microbit import *
import radio, music

radio.on()

def send_message(message):
    radio.send(message)
    display.show(Image.ARROW_N)
    sleep(1000)
    display.clear()

while True:
    if button_a.was_pressed():
        send_message("db1")
    if button_b.was_pressed():
        send_message("db2")
    message = radio.receive()
    if message == 'db1':
        music.play(music.ENTERTAINER)
    if message == 'db2':
        music.play(music.FUNERAL)