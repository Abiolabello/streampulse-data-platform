import requests
import pandas as pd

URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}


def fetch_crypto_data():
    response = requests.get(URL, params=PARAMS)
    response.raise_for_status()

    data = response.json()

    return pd.DataFrame(data)