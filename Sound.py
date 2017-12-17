# -*- coding: utf-8 -*-

import time

import RPi.GPIO as GPIO

#GPIO SETUP
channel = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#Alerts limits
max_freq_min = 2 # number of alerts per minute
max_num_hour = 10 # number of alerts per hour

alerts = []

def alert(bot_obj):
    bot = bot_obj
    def callback(channel):
        if GPIO.input(channel):
                bot.sendMessage(75413195, 'Sound alert!')
        #else:
        #        bot.sendMessage(75413195, 'Sound alert!')

    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

    # infinite loop
    while True:
            time.sleep(1)
