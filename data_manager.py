import gspread
from google.oauth2.service_account import Credentials
import os

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'keys.json'
# The ID  spreadsheet.
SAMPLE_SPREADSHEET_ID = os.environ.get('GSHEET_ID')

class DataManager:

    def __init__(self):
        #authorize account
        self.creds = Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.client = gspread.authorize(self.creds)

        # Create Spreadsheet
        self.spreadsheet = self.client.open('Flight Deals')
        self.worksheet = self.spreadsheet.worksheet('prices')


    def get_dest_data(self):
        result = self.worksheet.col_values(1)
        return result

    def get_lowest_price_data(self):
        result = self.worksheet.col_values(3)
        return result

    def update_dest_code(self, flight_codes):

        request = self.worksheet.update('B2:B10', flight_codes)
        return request

    def fill_low(self, update_low):
        request = self.worksheet.update('C2:C10', update_low)
        return request
