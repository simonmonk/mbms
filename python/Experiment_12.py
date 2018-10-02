from microbit import *
import radio

radio.on()
radio.config(power=7)

while True:
    if button_a.was_pressed():
        radio.send("test")
        display.show(Image.ARROW_N)
        sleep(1000)
        display.clear()
    message = radio.receive()
    if message == 'test':
        display.show(Image.YES)
        sleep(1000)
        display.clear()