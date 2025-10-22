import requests

class Crpyto:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.investment = 100

    def fetch_current_price(self):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={self.symbol}&vs_currencies=usd"
        data = requests.get(url).json()
        self.current_price = data[self.symbol]['usd']
