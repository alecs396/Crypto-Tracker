from calendar import timegm
from distutils.log import info
from time import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
import datetime
import apikey
import pandas as pd
import time

# Create empty list
crypto_time_list = []
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
            timestamp = pd.to_datetime(x['last_updated'])
            crypto_time_list.append(timestamp)
            crypto_name_list.append(x['name'])
            crypto_market_cap_list.append(x['quote']['USD']['market_cap'])
            crypto_price_list.append(x['quote']['USD']['price'])
            crypto_circulating_supply_list.append(x['circulating_supply'])
            crypto_symbol_list.append(x['symbol'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        
scrape()
time = pd.datetime.now()
# Store Data in dataframe
df['Time'] = crypto_time_list
df['Name'] = crypto_name_list
df['Market Cap'] = crypto_market_cap_list
df['Price'] = crypto_price_list
df['Circulating Supply'] = crypto_circulating_supply_list
df['Symbol'] = crypto_symbol_list
df.to_csv('data.csv', index=False, date_format='%Y-%m-%d %H:%M:%S')

print(df)

# fieldnames = ['Time', 'Name', 'Market Cap', 'Price', 'Circulating Supply', 'Symbol']

# with open('data2.csv', 'w') as csv_file:
#         csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         csv_writer.writeheader()
# while True:
#     scrape()
#     with open('data2.csv', 'a') as csv_file:
#         csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
#         info = {
#             "Time": crypto_time_list,
#             "Name": crypto_name_list,
#             "Market Cap": crypto_market_cap_list,
#             "Price": crypto_price_list,
#             "Circulating Supply": crypto_circulating_supply_list,
#             "Symbol": crypto_symbol_list
#         }
#         csv_writer.writerow(info)
#     time.sleep(60)