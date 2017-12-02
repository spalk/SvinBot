# -*- coding: utf-8 -*-

import datetime

import gspread   # Google Spreadsheets
from oauth2client.service_account import ServiceAccountCredentials

KEY_FILE = 'gdrive.json'

def gauth():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, scope)

def send_bp(bp):
    dt = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    try:
        gauth()
        
        gc = gspread.authorize(credentials)
        sheet = gc.open("Olyas Blood Pressure").sheet1

        dt_col = sheet.find('datetime').col
        val_col = sheet.find('value').col
        rows = len(sheet.get_all_values())

        sheet.update_cell(rows+1, dt_col, dt)
        sheet.update_cell(rows+1, val_col, bp)
        
        return True

    except:
        Return False