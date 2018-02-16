# -*- coding: utf-8 -*-

import os
import sys
import datetime
import json

DEFAULT_MESSAGE = '''*Here is what you can do:*
- to get a photo, use /get\_pic command;
- to get current condition in the room, use /get\_temp command.
- to send Olya's blood pressure in Google Docs, use  /bp command. 
Good luck!'''

def setStartTime():
    global startTime	
    startTime = datetime.datetime.now()

def getUptime():
    """
    Returns the number of seconds since the program started.
    """
    return datetime.datetime.now() - startTime

def read_access_list():
    '''
    Reading access.json file and returns access list as dict
    '''
    access_file_path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),'access.json')
    access_file = open(access_file_path)
    access_file_read = access_file.read()
    access_list = json.loads(access_file_read)
    access_file.close()
    return access_list

def check_access(user_id, command):
    '''
    Checking user id in access list and available commands for this particular 
    user. Returns True if ok or message if not ok. 
    '''

    global ACCESS_LIST

    uid = str(user_id)
    
    if uid in ACCESS_LIST.keys():
        if command[1:] in ACCESS_LIST[uid]:
            return True
        else:
            ACCESS_LIST = read_access_list()
            if command[1:] in ACCESS_LIST[uid]:
                return True
            else:
                return 'Sorry, this command is not available for you...'
    else:
        return 'Sorry, you are not in Access List. Ask admin to add your User ID: %s' % uid

    

ACCESS_LIST = read_access_list()