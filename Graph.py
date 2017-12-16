# -*- coding: utf-8 -*-

import os
import json
from urllib.request import urlopen 
import datetime

import pygal

CH_ID = "368739"  # thingspeak channel ID
GR_PATH = "img"

def get_data(field_num, field_name, results):
        url = 'https://api.thingspeak.com/channels/%s/fields/%s.json?results=%s&timezone=Europe/Moscow' % (CH_ID, field_num, results)
        feed = urlopen(url).read().decode('utf8')
        j = json.loads(feed)

        labs = []
        vals = []
        labels_num = 30
        labels_skip = results // labels_num
        count = 0
        for i in j['feeds']:
            count += 1
            if count % labels_skip == 0:
                labs.append(datetime.datetime.strptime(
                    i['created_at'], 
                    '%Y-%m-%dT%H:%M:%S+03:00'
                    ).strftime('%H:%M'))
            else: 
                labs.append('')
            vals.append(round(float(i[field_name]), 1))
        print(vals)
        return labs, vals


def get_pic(title, labels, data, pic_name):
        line_chart = pygal.Line(
            range = (min(data)-1, max(data)+1),
            x_label_rotation=90, 
            stroke_style={'width': 4}
            )
        line_chart.title = title
        line_chart.x_labels = labels
        line_chart.add(None, data)
        line_chart.render_to_png(pic_name)



def get_temp(usr_id, values_num = 60):
    l, v = get_data(1, 'field1', values_num)
    pic_name = "t-%s.png" % usr_id
    full_name = os.path.join(GR_PATH, pic_name)
    get_pic('Temperature', l, v, full_name)
    return full_name

def get_press(usr_id, values_num = 240):
    l, v = get_data(2, 'field2', values_num)
    pic_name = "img//p_%s.png" % usr_id
    get_pic('Pressure', l, v, pic_name)
    return pic_name

def get_humid(usr_id, values_num = 60):
    l, v = get_data(3, 'field3', values_num)
    pic_name = "img//h_%s.png" % usr_id
    get_pic('Humidity', l, v, pic_name)
    return pic_name


def get_temp_hum(usr_id):
    values_num = 120
    labels, t_vals = get_data(1, 'field1', values_num)
    labels, h_vals = get_data(3, 'field3', values_num)
    pic_name = "t+h_%s.png" % usr_id
    full_name = os.path.join(GR_PATH, pic_name)

    chart = pygal.Line(
        range = (min(t_vals)-1, max(t_vals)+1),
        secondary_range = (min(h_vals)-1, max(h_vals)+1),
        title='Temerature & Humidity',
        x_label_rotation=90, 
        stroke_style={'width': 4}
        )
    chart.x_labels = labels
    chart.add('T', t_vals)
    chart.add('H', h_vals, secondary=True)
    chart.render_to_png(full_name)
    return full_name
