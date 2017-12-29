import time

import RPi.GPIO as GPIO

# Colors contants:
OFF =   (0,0,0)
RED =   (1,0,0)
GREEN = (0,1,0)
BLUE =  (0,0,1)
PINK =  (1,0,1) 

#GPIO SETUP
rgb_pins = (5, 6, 13)
GPIO.setmode(GPIO.BCM)
for pin in rgb_pins:
    print(pin)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output (pin, 0)

def blink(color, times, delay):
    """
    Set color and blinking
    color - 3 items list (0 or 1 for RGB)
    times - of blinks
    delay - between blinks in seconds
    """
    while times > 0:
        times -= 1
        for i in range(3):
            GPIO.output (rgb_pins[i], color[i])
        time.sleep(delay)
        for i in range(3):
            GPIO.output (rgb_pins[i], 0)
        time.sleep(delay)


def three_green_blinks():
    blink(GREEN, 3, 0.1)

def one_pink_blink():
    blink(PINK, 1, 0.1)

def welcome_blink():
    blink(RED, 1, 0.1)
    blink(PINK, 1, 0.1)
    blink(BLUE, 1, 0.1)
    blink(PINK, 1, 0.1)
    blink(RED, 1, 0.1)
