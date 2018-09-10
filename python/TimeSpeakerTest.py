import speech

digits = ["no", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nienteen"]
tens = ["no", "no", "twenty", "thirty", "forty", "fifty"]

preamble = "The time is "
am = "aye em"
pm = "pee em"

minutes = 21
hours = 16

def speak_the_time():
    h = hours
    am_pm = am
    if h > 12:
        h = h - 12
        am_pm = pm
    if minutes == 0:
        speech.say(preamble + digits[h] + " " + am_pm + " exactly")
    else:
        if minutes < 20:
            speech.say(preamble + digits[h] + " " + digits[minutes] + " " + am_pm)
        else:
            mins_tens = int(minutes / 10)
            mins_units = minutes % 10
            speech.say(preamble + digits[h] + " " + tens[mins_tens] + " " + digits[mins_units] + " " + am_pm)
speak_the_time()