from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'credentials.json'
)

import pandas as pd

client = bigquery.Client(credentials=credentials)


project_id = 'projetosql-423912'
dataset_id = '1'
table_id = 'data_steam'

df = pd.read_csv('steam_game_sales.csv')

job = client.load_table_from_dataframe(df, f'{project_id}.{dataset_id}.{table_id}')

job.result()

print("Dados carregados com sucesso no BigQuery")
