from microbit import *

def set_servo_angle(pin, angle):
    duty = 26 + (angle * 102) / 180
    pin.write_analog(duty)

angle = 90
set_servo_angle(pin2, angle)

while True:
    if button_a.was_pressed() and angle >= 10:
        angle -= 10
        set_servo_angle(pin2, angle)
    if button_b.was_pressed() and angle <= 170:
        angle += 10
        set_servo_angle(pin2, angle)
        
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll(str(angle))