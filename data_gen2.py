from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df
import apikey

def get_price():
    client = Client(api_key=apikey.Pkey, api_secret=apikey.Skey)

    
    # This Function gets the Kline data for BTCUSDT
    candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)

    # Create Dataframe
    candles_data_frame = df(candles)
    candles_data_frame_date = candles_data_frame[0]
        
    final_date = []
        
    # Create Readable dates for datafram
    for time in candles_data_frame_date.unique():
        readable = datetime.fromtimestamp(int(time/1000))  # Turn into a readable date. Binance does things in miliseconds hence /1000
        final_date.append(readable)
        
    candles_data_frame.pop(0)
    candles_data_frame.pop(11)
        
    # Create Dataframe for Dates
    dataframe_final_date = df(final_date)
    dataframe_final_date.columns = ['date']
        
    # Join the two DataFrames together
    final_dataframe = candles_data_frame.join(dataframe_final_date)
        
    # Set index to date
    final_dataframe.set_index('date', inplace=True)
    # Label all columns according to python-binance API
    final_dataframe.columns = ['open', 'high', 'low', 'close', 'volume', 'close_time', 'asset_volume', 'trade_number', 'taker_buy_base', 'taker_buy_quote']
    
    return final_dataframe
        
print(get_price())
    



    


