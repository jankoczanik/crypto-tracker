import requests
import time
from crypto import Crpyto
from graph import Graph

def get_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 4,
        "page": 1
    }

    attempt = 0
    while attempt < 10:
        attempt += 1
        response = requests.get(url, params=params).json()
        if "status" in response and "error_code" in response['status'] and response['status']['error_code'] == 429:
            print(f"[Crypto List] Rate limit exceeded. ({attempt}/10)")
            if attempt == 10:
                exit()
        else:
            print('[Crypto List] Successfully fetched data.')
            cryptos = [(c['name'], c['id']) for c in response]
            return [Crpyto(name, symbol) for name, symbol in cryptos]
        time.sleep(5)

def main():

    cryptos = get_cryptos()
    graph = Graph()

    for crypto in cryptos:
        crypto.fetch_last_years_prices()

    graph.plot_cryptos(cryptos)

if __name__ == "__main__":
    main()