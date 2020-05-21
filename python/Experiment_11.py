from microbit import *
import radio

busy = False
last_busy_flip = 0
busy_period = 600000
last_log_time = 0
log_period = 20000

while True:
    if busy:
        display.on()
        radio.on()
        display.show("Busy")
    else:
        display.off()
        radio.off()
    now = running_time()
    if now > last_busy_flip + busy_period:
        busy = not busy
        last_busy_flip = now
    now = running_time()
    if now > last_log_time + log_period:
        print((temperature(), busy * 10))
        last_log_time = now
