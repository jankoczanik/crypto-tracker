import matplotlib.pyplot as plt
import datetime

class Graph:
    def __init__(self):
        pass

    def plot_cryptos(self, cryptos):
        plt.figure(figsize=(12, 6))
        for crypto in cryptos:
            dates = [datetime.datetime.fromtimestamp(ts / 1000) for ts, _ in crypto.prices]
            prices = [price for _, price in crypto.prices]

            monthly_dates = dates[::30]
            monthly_prices = prices[::30]

            initial_price = monthly_prices[0]
            monthly_prices = [(price / initial_price) * 100 for price in monthly_prices]

            plt.plot(monthly_dates, monthly_prices, label=crypto.name)

        plt.title("Crypto Performance Over Last Year")
        plt.xlabel("Date")
        plt.ylabel("Price in USD")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()