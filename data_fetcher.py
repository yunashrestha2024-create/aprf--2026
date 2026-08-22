import requests
import pandas as pd

def fetch_world_bank_data(indicator, country="NPL", per_page=5):
    try:
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page={per_page}"
        response = requests.get(url, timeout=10)
        data = response.json()
        rows = data[1]
        return {int(row['date']): row['value'] for row in rows if row['value'] is not None}
    except:
        return None
