# -*- coding: utf-8 -*-

import datetime

from Adafruit_BME280 import *

def  get_cur_vals():
    sensor = BME280(mode=BME280_OSAMPLE_8, address = 0x76)

    degrees = '%.1f' %  sensor.read_temperature()
    pascals = sensor.read_pressure()
    mmhg = '%.1f' % (pascals * 0.00750062)
    humidity = '%.1f' % sensor.read_humidity()
    
    return degrees, mmhg, humidity 


def build_msg(degrees, mmhg, humidity):
    degree_sign = u'\N{DEGREE SIGN}'
    dt_now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

    msg_txt = '''*Conditions for %s*
Temperature:  %s %sC
Humidity:         %s %% 
Pressure:         %s mmHg
''' % (dt_now, degrees, degree_sign, humidity, mmhg)

    return msg_txt
		

def get_msg(): 
    temp, press, hum = get_cur_vals()
    
    return build_msg(temp, press, hum)