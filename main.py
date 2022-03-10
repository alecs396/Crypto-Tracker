from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import apikey
import time
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def plotData():
    plt.style.use('fivethirtyeight')
    
    x_vals = []
    y_vals = []

    index = count()
    
    def animate(i):
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 5))
    
        plt.cla()
        plt.plot(x_vals, y_vals)
    
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    
    plt.tight_layout()
    plt.show()

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
                symbol = x['symbol']
                market_cap = x['quote']['USD']['market_cap']
                print(symbol, market_cap)
                # print(x['symbol'], x['quote']['USD']['market_cap'])
            print("\n")
            print(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        time.sleep(60)
        
        
    # try:
    #     response = session.get(url, params=parameters)
    #     data = json.loads(response.text)
    #     coins = data['data']
    #     for x in coins:
    #         print(x['symbol'], x['quote']['USD']['price'])
    #     print("\n")
    # except (ConnectionError, Timeout, TooManyRedirects) as e:
    #     print(e)
    
while True: 
    getData()
    plotData()
    time.sleep(60)