import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("HTN 2021").sheet1

# Extract and print all of the values

sheet.update_cell(2, 1, "Jeffrey Luo NO")

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)