from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import apikey
import time
import data_gen
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


plt.style.use('fivethirtyeight')
data = pd.read_csv('data.csv')

x = data['Symbol']
y1 = data['Market Cap']
plt.bar(x, y1, color='#444444', label="Market Cap")


plt.legend()
plt.title("Market Cap of Top 10 Coins")
plt.xlabel("Coin")
plt.ylabel("Market Cap (USD Millions)")
plt.tight_layout()
plt.show()