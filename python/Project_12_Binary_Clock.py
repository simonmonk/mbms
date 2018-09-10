from microbit import *


# hhhhh
# m
# mmmmm
# s
# sssss

sec_leds = [[4, 4], [3, 4], [2, 4], [1, 4], [0, 4], [0, 3]]
min_leds = [[4, 2], [3, 2], [2, 2], [1, 2], [0, 2], [0, 1]]
hour_leds = [[4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]

hours = 16
minutes = 46
seconds = 0

adjust = -10

def display_binary(value, num_bits, leds):
    v = value
    for i in range(0, num_bits):
        v_bit = v % 2
        display.set_pixel(leds[i][0], leds[i][1], int(v_bit * 9))
        v = int(v / 2)
        
last_time = 0        
tick = 1000 + adjust

def update_time():
    global hours, minutes, seconds
    seconds += 1
    if seconds > 59:
        seconds = 0
        minutes += 1
        if minutes > 59:
            minutes = 0
            hours += 1
            if hours > 23:
                hours = 0
        
def display_time():
    display_binary(seconds, 6, sec_leds)
    display_binary(minutes, 6, min_leds)
    display_binary(hours, 5, hour_leds)    
        
while True:
    if button_a.is_pressed():
        tick = 10
    else:
        tick = 1000 + adjust
    now = running_time()
    elapsed_ms = now - last_time
    if elapsed_ms >= tick:
        update_time()
        display_time()
        last_time = now