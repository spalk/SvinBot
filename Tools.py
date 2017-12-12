# -*- coding: utf-8 -*-

import datetime
import json

DEFAULT_MESSAGE = '''*Here is what you can do:*
- to get a photo, use /get\_pic command;
- to get current condition in the room, use /get\_temp command.
- to send Olya's blood pressure in Google Docs, use  /bp command. 
Good luck!'''

access_file = open('access.json').read()
ACCESS_LIST = json.loads(access_file)

def setStartTime():
    global startTime	
    startTime = datetime.datetime.now()

def getUptime():
    """
    Returns the number of seconds since the program started.
    """
    return datetime.datetime.now() - startTime


def check_access(user_id, command):
    uid = str(user_id)
    if uid in ACCESS_LIST.keys():
        if command[1:] in ACCESS_LIST[uid]:
            return True
        else:
            return 'Sorry, this command is not available for you...'
    else:
        return 'Sorry, you are not in Access List. Ask admin to add your User ID: %s' % uid

    

