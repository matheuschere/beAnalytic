import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://store.steampowered.com/app/1672970/'

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('div', class_='apphub_AppName').text.strip()
    price = soup.find('div', class_='game_purchase_price').text.strip()
    discount = soup.find('div', class_='discount_pct').text.strip()
    rating = soup.find('span', class_='game_review_summary').text.strip()
    release_date = soup.find('div', class_='date').text.strip()

    df = pd.DataFrame({
        'name': [name],
        'price': [price],
        'discount': [discount],
        'rating': [rating],
        'release_date': [release_date]
    })

    df.to_csv('steam_game_sales.csv', index=False)

    print("Dados extraídos e salvos com sucesso em 'steam_game_sales.csv'")

except Exception as e:
    print("Erro ao processar a requisição:", e)
