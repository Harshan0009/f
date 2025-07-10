import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st

# Define scope for Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# ✅ Read credentials directly from secrets (no json.dumps needed)
json_key = dict(st.secrets["google_service_account"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_key, scope)

# Authorize client and access spreadsheet
client = gspread.authorize(creds)
sheet = client.open("InOffice Data")  # Change name if your sheet is different

def read_sheet(sheet_name):
    worksheet = sheet.worksheet(sheet_name)
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

def write_sheet(sheet_name, df):
    worksheet = sheet.worksheet(sheet_name)
    worksheet.clear()
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
