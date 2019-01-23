from microbit import *
import speech

digits = ["no", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nienteen"]
tens = ["no", "no", "twenty", "thirty", "forty", "fifty"]

preamble = "The time is "
am = "aye em"
pm = "pee em"

hours = 8
minutes = 26
seconds = 0
adjust = -10

last_time = 0        
tick = 1000 + adjust

def update_time(elapsed_seconds):
    global hours, minutes, seconds
    seconds += elapsed_seconds
    if seconds > 59:
        seconds = elapsed_seconds - 1
        minutes += 1
        if minutes > 59:
            minutes = 0
            hours += 1
            speak_the_time()
            if hours > 23:
                hours = 0
        
def speak_the_time():
    h = hours
    am_pm = am
    if h >= 12:
        am_pm = pm
    if h > 12:
        h = h - 12
    if minutes == 0:
        # The time is twelve pm exactly
        speech.say(preamble + digits[h] + " " + am_pm + " exactly")
    else:
        if minutes < 10:
            # The time is twelve o four pm
            speech.say(preamble + digits[h] + " o " + digits[minutes] + " " + am_pm)        
        elif minutes < 20:
            # The time is twelve eighteen pm
            speech.say(preamble + digits[h] + " " + digits[minutes] + " " + am_pm)
        else:
            mins_tens = int(minutes / 10)
            mins_units = minutes % 10
            if mins_units == 0:
                # The time is twelve twenty pm
                speech.say(preamble + digits[h] + " " + tens[mins_tens] + " " + am_pm)
            else:
                # The time is twelve twenty four pm
                speech.say(preamble + digits[h] + " " + tens[mins_tens] + " " + digits[mins_units] + " " + am_pm)
            
def blink():
    display.show(Image.HEART)
    sleep(100)
    display.clear()
        
while True:
    if button_b.is_pressed():
        speak_the_time()
    now = running_time()
    elapsed_ms = now - last_time
    if elapsed_ms >= tick:
        elapsed_seconds = int(elapsed_ms / tick)
        update_time(elapsed_seconds)
        blink()
        last_time = now
        
      