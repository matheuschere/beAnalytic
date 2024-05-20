import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import gspread
from gspread_dataframe import set_with_dataframe

bigquery_credentials = service_account.Credentials.from_service_account_file(
    'credentials.json'
)

client = bigquery.Client(credentials=bigquery_credentials, project='projetosql-423912')

query = """
SELECT * FROM `projetosql-423912.1.data_steam`
"""

query_job = client.query(query)
df = query_job.to_dataframe()

sheets_credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)

gc = gspread.authorize(sheets_credentials)
spreadsheet = gc.open('SheetsMatheus')
worksheet = spreadsheet.sheet1  

worksheet.clear()

set_with_dataframe(worksheet, df)

print("Dados exportados com sucesso para o Google Sheets")
