# -*- coding: utf-8 -*-

import time
import datetime
import json
import threading

import telepot

import Pic, Env, Health, Tools, Graph, Sound

t_key_file = open('telegram.json').read()
TELEGRAM_KEY = json.loads(t_key_file)['token']

Tools.setStartTime()

bot_mode = 0

def handle(msg):
	global bot_mode

	user_id = msg['from']['id']
	chat_id = msg['chat']['id']
	command = msg['text']
	dtnow = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
	print ('%s - %s - Got command: %s' % (dtnow, user_id, command))

	if command == '/get_pic':
		access = Tools.check_access(user_id, command)
		if access == True:
			pic = Pic.get_pic(user_id)
			pic_file = open(pic,'rb')
			bot.sendPhoto(chat_id, pic_file)
		else:
			bot.sendMessage(chat_id, access)
		bot_mode = 0

	elif command == '/get_temp':
		msg_txt = Env.get_msg()
		bot.sendMessage(chat_id, str(msg_txt), 'Markdown')
		bot_mode = 0

	elif command == '/uptime':
		access = Tools.check_access(user_id, command)
		if access == True:
			bot.sendMessage(chat_id, str(Tools.getUptime()))
		else:
			bot.sendMessage(chat_id, access)
		bot_mode = 0

	elif command == '/get_temp_graph':
		graph_pic = Graph.get_temp(user_id)
		pic_file = open(graph_pic,'rb')
		bot.sendPhoto(chat_id, pic_file)
		bot_mode = 0

	elif command == '/get_hum_graph':
		graph_pic = Graph.get_humid(user_id)
		pic_file = open(graph_pic,'rb')
		bot.sendPhoto(chat_id, pic_file)
		bot_mode = 0

	elif command == '/get_press_graph':
		graph_pic = Graph.get_press(user_id)
		pic_file = open(graph_pic,'rb')
		bot.sendPhoto(chat_id, pic_file)
		bot_mode = 0

	elif command == '/get_t_h':
		graph_pic = Graph.get_temp_hum(user_id)
		pic_file = open(graph_pic,'rb')
		bot.sendPhoto(chat_id, pic_file)
		bot_mode = 0

	elif command == '/bp':
		access = Tools.check_access(user_id, command)
		if access == True:
			bot_mode = 'body_pressure'
			msg_txt = '''Input your blood pressure in any format...'''
			bot.sendMessage(chat_id,msg_txt)
		else:
			bot.sendMessage(chat_id, access)
			bot_mode = 0

	elif command == '/w':
		access = Tools.check_access(user_id, command)
		if access == True:
			bot_mode = 'weight'
			msg_txt = '''Input your weight in any format...'''
			bot.sendMessage(chat_id,msg_txt)
		else:
			bot.sendMessage(chat_id, access)
			bot_mode = 0

	else:
		if bot_mode == 'body_pressure':
			result = Health.send_bp(command)
			if result:
				bot.sendMessage(chat_id, "Successful!")
			else: 
				bot.sendMessage(chat_id, "Something wrong :(")
			bot_mode = 0
		elif bot_mode == 'weight':
			result = Health.send_w(command)
			if result:
				bot.sendMessage(chat_id, "Successful!")
			else: 
				bot.sendMessage(chat_id, "Something wrong :(")
			bot_mode = 0
		else:
			msg_txt = Tools.DEFAULT_MESSAGE
			bot.sendMessage(chat_id, msg_txt, 'Markdown')
			bot_mode = 0

bot = telepot.Bot(TELEGRAM_KEY)
bot.message_loop(handle)
#Sound.alert(bot)
while 1:
    time.sleep(10)
