
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1_ZqRLvGnydj4gZC0seHJcOF68dZ3Klg5KUXGNHyw0bo'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Reto1!A1:D16").execute()

requests=[]

requests.append({
    'updateCells':{
                'rows':{
                    'values':[
                        {
                            'pivotTable':{
                                'source':{
                                    'sheetId':'0',
                                    'startRowIndex':0,
                                    'startColumnIndex':0,
                                    'endRowIndex':16,
                                    'endColumnIndex':4
                                },

                                'rows':[


                                        {
                                        'sourceColumnOffset':0,
                                        'sortOrder':'ASCENDING',
                                        # 'repeatHeading': True,
                                        'label': 'Author'
                                        },

                                        {
                                        'sourceColumnOffset':1,
                                        'sortOrder':'ASCENDING',
                                        # 'repeatHeading': True,
                                        'label': 'Sentiment'
                                        }
   

                                ],

                                'columns':[
                                    {
                                        'sourceColumnOffset':2,
                                        'sortOrder':'ASCENDING',
                                        # 'repeatHeading': True,
                                        'label':'Country'
                                    },

                                    {
                                        'sourceColumnOffset':3,
                                        'sortOrder':'ASCENDING',
                                        # 'repeatHeading': True,
                                        'label':'Theme'
                                    }
                                ],

                                'values':[
                                    {
                                        'sourceColumnOffset':3,
                                        'summarizeFunction':'COUNTA',
                                        'name':'Count Unique of Country'
                                    }
                                ],

                                'valueLayout':'HORIZONTAL'
                            }
                        }
                    ]
                },

                'start':{
                    'sheetId':'1587252686',
                    'rowIndex':10,
                    'columnIndex':0
                },

                'fields':'pivotTable'
            }
})
body = {
    'requests': requests
}


response = service.spreadsheets() \
    .batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=body).execute()

print(response)