from microbit import *
import random

n = 5

def run_full_test():
    print("TEST 1 - USING your hand")
    t_hand = run_test()
    print("The average time using your hand was " + str(t_hand) + " ms")
    print("Now repeat the test for your foot")
    t_foot = run_test()
    print("The average time using your foot was " + str(t_foot) + " ms")
    d_hand = int(input("Enter the distance from the back of your neck to your fingers in cm: "))
    d_foot = int(input("Enter the distance from the back of your neck to your toes in cm: "))
    thinking_time = (d_hand * t_foot - d_foot * t_hand) / (d_hand - d_foot)
    transmission_speed = 10 * (t_foot - thinking_time) / d_foot
    print("Thinking time (ms): " + str(thinking_time))
    print("Transmission speed (m/s): " + str(transmission_speed))

def run_test():
    print("Hold the switch down while cross is showing.")
    print("Release momentarily when the display blanks.")
    print("Repeat " + str(n) + " times.")
    input("Press ENTER when ready to start the test")
    total = 0
    for i in range(0, n):
        t = get_reaction_time()
        if t > 10:
            print(t)
            total += t
        else:
            print("You let go too soon")
    return total / n
            
def get_reaction_time():
    display.show(Image.NO)
    sleep(random.randint(3000, 7000))
    display.clear()
    t0 = running_time()
    while button_a.is_pressed():
        pass
    t1 = running_time()
    t = t1 - t0
    return t
        
run_full_test()
        
        
