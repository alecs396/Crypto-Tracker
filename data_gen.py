from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
import datetime
import apikey
import pandas as pd

# Create empty lists
crypto_name_list = []
crypto_market_cap_list = []
crypto_price_list = []
crypto_circulating_supply_list = []
crypto_symbol_list = []

# Create empty dataframe to organize data
df = pd.DataFrame()

def scrape():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    # Set Parameters of what crypto to track and what currency the price is displayed as.
    parameters = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': apikey.key
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        coins = data['data']
        # Append data to lists
        for x in coins:
                    crypto_name_list.append(x['name'])
                    crypto_market_cap_list.append(x['quote']['USD']['market_cap'])
                    crypto_price_list.append(x['quote']['USD']['price'])
                    crypto_circulating_supply_list.append(x['circulating_supply'])
                    crypto_symbol_list.append(x['symbol'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        
scrape()

# Store Data in dataframe
df['Name'] = crypto_name_list
df['Market Cap'] = crypto_market_cap_list
df['Price'] = crypto_price_list
df['Circulating Supply'] = crypto_circulating_supply_list
df['Symbol'] = crypto_symbol_list
df.to_csv('data.csv')

#show data
print(df)
