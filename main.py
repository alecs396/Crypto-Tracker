from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import apikey
import data_gen
import time
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def plotData():
    data = pd.read_csv('data.csv')
    plt.style.use('fivethirtyeight')
    
    x_vals = data['Time']
    y_vals = data['Price']

    plt.plot(x_vals, y_vals)
    index = count()
    
    # def animate(i):
    #     data = pd.read_csv('data.csv')
    #     x = data['Time']
    #     y1 = data['Market Cap']
    
    #     plt.cla()
    #     plt.plot(x, y1)
    
    # ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    
    plt.tight_layout()
    plt.show()

plotData()