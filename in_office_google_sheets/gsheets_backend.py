import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

sheet = client.open("InOffice Data")

def read_sheet(sheet_name):
    worksheet = sheet.worksheet(sheet_name)
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

def write_sheet(sheet_name, df):
    worksheet = sheet.worksheet(sheet_name)
    worksheet.clear()
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
