from microbit import *

seconds = 0
last_time = 0

while True:
    now = running_time()
    elapsed_ms = now - last_time
    if elapsed_ms >= 1000:
        seconds += 1
        last_time = now
    if button_a.was_pressed():
        display.scroll(str(seconds))
    if button_b.was_pressed():
        seconds = 0
        display.show("0")
        sleep(100)
        display.clear()