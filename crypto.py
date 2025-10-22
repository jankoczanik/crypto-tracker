import requests
import time

API_URL = "https://api.coingecko.com/api/v3"

class Crpyto:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def fetch_current_price(self):
        url = f"{API_URL}/price?ids={self.symbol}&vs_currencies=usd"
        data = requests.get(url).json()
        self.current_price = data

    def fetch_last_years_prices(self):
        url = f"{API_URL}/coins/{self.symbol}/market_chart"
        params = {"vs_currency": "usd", "days": 360}

        attempt = 0
        while attempt < 10:
            attempt += 1
            response = requests.get(url, params=params).json()
            if "status" in response and "error_code" in response['status'] and response['status']['error_code'] == 429:
                print(f'[{self.name}] Rate limit exceeded. ({attempt}/10)')
                if attempt == 10:
                    exit()
            else:
                self.prices = response['prices']
                print(f'[{self.name}] Successfully fetched data.')
                break
            time.sleep(5)
                
        
    
