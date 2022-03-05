from wsgiref import headers
import apikey
import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'X-CMC_PRO_API_KEY' : apikey.key,
    'Accepts' : 'application/json'
}

# Set Parameters of what crypto to track and what currency the price is displayed as.
params = {
    'start' : '1',
    'limit' : '10',
    'convert' : 'USD'
}

json = requests.get(url, params=params, headers=headers).json()
print(json)