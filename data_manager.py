from googleapiclient.discovery import build
from google.oauth2 import service_account
import os



SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'
# The ID  spreadsheet.
SAMPLE_SPREADSHEET_ID = os.environ.get('GSHEET_ID')

class DataManager:

    def __init__(self):
        # creds = None
        self.creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        self.service = build('sheets', 'v4', credentials=self.creds)

        # Call the Sheets API
        self.sheet = self.service.spreadsheets()

    def get_destenation_data(self):
        result = self.sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range='prices!A2:A10').execute()
        values = result.get('values', [])
        return values


    def update_destenation_code(self, flight_codes):

        request = self.sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range='prices!B2:B10',
                                        valueInputOption='USER_ENTERED',
                                        body={'values':flight_codes}).execute()
        return request

