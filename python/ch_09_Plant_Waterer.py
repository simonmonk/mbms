from microbit import *

dryness = 0
dry_threshold = 500
on_time_ms = 10000
check_period_ms = 3600000
dont_check_until = 0

def water_the_plant():
    pin0.write_digital(1)
    display.show(Image.ARROW_S)
    sleep(on_time_ms)
    pin0.write_digital(0)
    
def check_dryness():
    global dryness
    pin1.write_digital(1)
    dryness = pin2.read_analog()
    pin1.write_digital(1)
    
def bargraph(a):
    display.clear()
    for y in range(0, 5):
        if a > y:
            for x in range(0, 5):
                display.set_pixel(x, 4-y, 9)
    
while True:
    if button_a.was_pressed():
        check_dryness()
        display.scroll(str(dryness))
        bargraph(dryness / 200)
    if button_b.was_pressed():
        water_the_plant()
        check_dryness()
        bargraph(dryness / 200)
    if running_time() > dont_check_until:
        check_dryness()
        if dryness > dry_threshold:
            water_the_plant()
        dont_check_until = running_time() + check_period_ms
        bargraph(dryness / 200)