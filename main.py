from pkgutil import extend_path
from urllib import response
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import apikey
import time


def getData(): 
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
    
    while True:
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            coins = data['data']
            for x in coins:
                print(x['symbol'], x['quote']['USD']['price'])
            print("\n")
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        time.sleep(60)
        
    
    # json = requests.get(url, params=params, headers=headers).json()

    # coins = json['data']
    
    # while True:
    #     for x in coins:
    #         print(x['symbol'], x['quote']['USD']['price'])
        
getData()