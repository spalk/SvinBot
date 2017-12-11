# -*- coding: utf-8 -*-

import os
import json
from urllib.request import urlopen 
import datetime

import pygal

CH_ID = "368739"
GR_PATH = "img"

def get_data(field_num, field_name, results):
        url = 'https://api.thingspeak.com/channels/%s/fields/%s.json?results=%s&timezone=Europe/Moscow' % (CH_ID, field_num, results)
        feed = urlopen(url).read().decode('utf8')
        j = json.loads(feed)

        labs = []
        vals = []
        for i in j['feeds']:
                labs.append(datetime.datetime.strptime(
                    i['created_at'], 
                    '%Y-%m-%dT%H:%M:%SZ'
                    ).strftime('%H:%M'))
                vals.append(float(i[field_name]))
        del labs[::2]
        return labs, vals


def get_pic(title, labels, data, pic_name):
        line_chart = pygal.Line(
            x_label_rotation=90, 
            #interpolate='lagrange',
            stroke_style={'width': 5} #, 'linecap': 'round', 'linejoin': 'round'}
            )
        line_chart.title = title
        line_chart.x_labels = labels
        line_chart.add(None, data)
        line_chart.render_to_png(pic_name)



def get_temp(usr_id, values_num = 30):
    l, v = get_data(1, 'field1', values_num)
    pic_name = "t-%s.png" % usr_id
    full_name = os.path.join(GR_PATH, pic_name)
    get_pic('Temperature', l, v, full_name)
    return full_name

def get_press(usr_id, values_num = 100):
    l, v = get_data(2, 'field2', values_num)
    pic_name = "img//p_%s.png" % usr_id
    get_pic('Pressure', l, v, pic_name)
    return pic_name

def get_humid(usr_id, values_num = 30):
    l, v = get_data(3, 'field3', values_num)
    pic_name = "img//h_%s.png" % usr_id
    get_pic('Humidity', l, v, pic_name)
    return pic_name


def get_temp_hum(usr_id):
    values_num = 60
    labels, t_vals = get_data(1, 'field1', values_num)
    labels, h_vals = get_data(3, 'field3', values_num)
    pic_name = "t+h_%s.png" % usr_id
    full_name = os.path.join(GR_PATH, pic_name)

    chart = pygal.Line(
        title='Temerature & Humidity',
        x_label_rotation=90, 
        #interpolate='lagrange',
        stroke_style={'width': 5}
        )
    chart.x_labels = labels
    chart.add('T', t_vals)
    chart.add('H', h_vals, secondary=True)
    chart.render_to_png(full_name)
    return full_name
