from microbit import *
import random
import speech

eye_angles = [50, 140, 60, 90, 140]

sentences = [
    "Hello my name is Mike",
    "What is your name",
    "I am looking at you",
    "Exterminate exterminate exterminate",
    "Number Five is alive",
    "I cant do that Dave",
    "daisee daisee give me your answer do"
    ]

lips0 = Image("00000:"
             "00000:"
             "99999:"
             "00000:"
             "00000")
             
lips1 = Image("00000:"
             "00900:"
             "99099:"
             "00900:"
             "00000")
             
lips2 = Image("00000:"
             "09990:"
             "99099:"
             "09990:"
             "00000")
             
lips = [lips0, lips1, lips2]

def set_servo_angle(pin, angle):
    duty = 26 + (angle * 51) / 90
    pin.write_analog(duty)
    
def speak(sentence):
    words = sentence.split()
    for i in range(0, len(words)):
        display.show(random.choice(lips))
        speech.say(words[i])
    display.show(lips0)
    
def act():
    set_servo_angle(pin2, random.choice(eye_angles))
    sleep(300)
    speak(random.choice(sentences))
    set_servo_angle(pin2, 90)
    sleep(2000)
    
base_z = 0

while True:
    new_z = abs(accelerometer.get_z())
    if abs(new_z - base_z) > 20:
        base_z = new_z
        act()
    if random.randint(0, 1000) == 0:
        act()
    sleep(50)