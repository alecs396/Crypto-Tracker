import pandas as pd
import mplfinance as mpf
from data_gen import get_price

def plot_candles():
    data = pd.read_csv('data.csv', index_col=0, parse_dates=True)
    # data.date = pd.to_datetime(data.date)
    data.info()
    mpf.plot(data, 
             type='candle',
             style='blueskies',
             tight_layout=True)