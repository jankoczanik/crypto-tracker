# Crypto Investment Tracker

A Python application that fetches the top cryptocurrencies an visualizes hypothetical profits if $100 was invested 1 year ago

## Author:

Developed by [Janko](https://github.com/jankoczanik)

## Features:

- Fetches the top 4 cryptocurrencies from the CoinGecko API
- Normalizes prices from the last year to simulate a $100 investment
- Plots interactive line graphs displaying monthly performance
- Automatic retry attempts on API rate limits

## Requirements:

- Python 3.10+
- `requests`
- `matplotlib`

## How to Use:

1. Clone the repository
2. Navigate to the project folder
3. Install required Python packages

`pip install requests`
`pip install requests matplotlib`

4. Run the script

`python main.py`

5. Interact with the automatically generated graph
