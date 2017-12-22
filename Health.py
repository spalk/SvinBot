# -*- coding: utf-8 -*-

import datetime

import gspread   # Google Spreadsheets
from oauth2client.service_account import ServiceAccountCredentials

KEY_FILE = 'gdrive.json'

def gauth():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, scope)
    gc = gspread.authorize(credentials)
    
    return gc


def send_bp(bp):
    result = _send('BP', bp)
    if result:
        return True
    else: 
        return False


def send_w(w):
    result = _send('Weight', w)
    if result:
        return True
    else: 
        return False


def _send(sheet, value):
    dt = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    try:
        gc = gauth()
        
        sheet = gc.open("Olyas Blood Pressure").worksheet(sheet)

        dt_col = sheet.find('datetime').col
        val_col = sheet.find('value').col
        rows = len(sheet.get_all_values())

        sheet.update_cell(rows+1, dt_col, dt)
        sheet.update_cell(rows+1, val_col, value)
    
        return True

    except Exception as e: 
        print(e)
        return False
