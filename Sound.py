# -*- coding: utf-8 -*-

import datetime
import time

import RPi.GPIO as GPIO

#GPIO SETUP
channel = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#Alerts limits
max_freq_min = datetime.timedelta(minutes = 2)  # number of alerts per minute
max_freq_hour = datetime.timedelta(minutes = 15)  # number of alerts per hour
max_alerts_num = 3  # number of alerts

alerts_stack = [datetime.datetime.now()-datetime.timedelta(hours = 1)]
count = 0

def alert(bot_obj):
    global count
    bot = bot_obj
    def callback(channel):
        global count
        if GPIO.input(channel):
            count += 1
            now = datetime.datetime.now()
            if (now - alerts_stack[0]) > max_freq_hour:
                if (now - alerts_stack[-1]) > max_freq_min:
                    if len(alerts_stack) == max_alerts_num: 
                        alerts_stack.pop(0)
                    alerts_stack.append(now)
                    bot.sendMessage(75413195, 'Sound alert! [%s]' % count)
                else:
                    print('max min too oft [%s]' % count)
            else:
                print('max hour too oft [%s]' % count)
  
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

    # infinite loop
    while True:
        time.sleep(1)
