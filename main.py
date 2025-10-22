import requests
from crypto import Crpyto

def get_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1
    }
    response = requests.get(url, params=params).json()
    cryptos = [(c['name'], c['id']) for c in response]
    return [Crpyto(name, symbol) for name, symbol in cryptos]

def main():

    cryptos = get_cryptos()

    for crypto in cryptos:
        crypto.fetch_current_price()
        print(crypto.current_price)

if __name__ == "__main__":
    main()