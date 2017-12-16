# -*- coding: utf-8 -*-

import os
import time

import picamera

PIC_PATH = 'img'
PIC_NAME = 'pic_%s.jpg'

def get_pic(user_id):
    camera = picamera.PiCamera()
    camera.rotation = 90
    time.sleep(1)
    full_name = os.path.join(PIC_PATH, PIC_NAME % user_id)
    camera.capture(full_name)
    time.sleep(1)
    camera.close()
    del camera
    return full_name