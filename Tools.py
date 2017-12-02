# -*- coding: utf-8 -*-

DEFAULT_MESSAGE = '''*Here is what you can do:*
- to get a photo, use /get\_pic command;
- to get current condition in the room, use /get\_temp command.
- to send Olya's blood pressure in Google Docs, use  /bp command. 
Good luck!'''


def check_access(command, user_id):
    return 1