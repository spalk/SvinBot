# -*- coding: utf-8 -*-

import time
import datetime
import json

import telepot

import Pic, Env, Health, Tools

t_key_file = open('telegram.json').read()
TELEGRAM_KEY = json.loads(t_key_file)['token']

bot_mode = 0

def handle(msg):
	global bot_mode

	user_id = msg['from']['id']
	chat_id = msg['chat']['id']
	command = msg['text']
	print 'Got command: %s' % command

	if command == '/get_pic':
		pic = Pic.get_pic(user_id)
		pic_file = open(pic,'rb')
	    	bot.sendPhoto(chat_id, pic_file)
		bot_mode = 0

	elif command == '/get_temp':
		msg_txt = Env.get_msg()
		bot.sendMessage(chat_id, str(msg_txt), 'Markdown')
		bot_mode = 0

	elif command == '/bp':	
		bot_mode = 'body_pressure'
		msg_txt = '''Input your blood pressure in any format...'''
		bot.sendMessage(chat_id,msg_txt)

	else:
		if bot_mode == 'body_pressure':
			result = Health.send_bp(command)
			if result:
				bot.sendMessage(chat_id, "Successful!")
			else: 
				bot.sendMessage(chat_id, "Somethign wrong :(")
			bot_mode = 0
		else:
			msg_txt = Tools.DEFAULT_MESSAGE
			bot.sendMessage(chat_id, msg_txt, 'Markdown')
			bot_mode = 0


bot = telepot.Bot(TELEGRAM_KEY)
bot.message_loop(handle)
while 1:
    time.sleep(10)
