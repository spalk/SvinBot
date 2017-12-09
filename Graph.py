# -*- coding: utf-8 -*-

import json
import urllib2 
import datetime

import pygal

CH_ID = "368739"

def get_data(field_num, field_name, results):
        url = 'https://api.thingspeak.com/channels/%s/fields/%s.json?results=%s' % (CH_ID, field_num, results)
        feed = urllib2.urlopen(url)
        j = json.load(feed)

        labs = []
        vals = []
        for i in j['feeds']:
                labs.append(datetime.datetime.strptime(i['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%H:%M'))
                vals.append(float(i[field_name]))
        return labs, vals


def get_pic(title, labels, data, pic_name):
        line_chart = pygal.Line()
        line_chart.title = title
        line_chart.x_labels = labels
        line_chart.add(None, data)
        line_chart.render_to_png(pic_name)



def get_temp(usr_id, values_num = 30):
    l, v = get_data(1, 'field1', values_num)
    pic_name = "img/t_%s.png"
    get_pic('Temperature', l, v)
    return pic_name

def get_press(usr_id, values_num = 60):
    l, v = get_data(1, 'field2', values_num)
    pic_name = "img/p_%s.png"
    get_pic('Pressure', l, v)
    return pic_name

def get_humid(usr_id, values_num = 30):
    l, v = get_data(1, 'field3', values_num)
    pic_name = "img/h_%s.png"
    get_pic('Humidity', l, v)
    return pic_name