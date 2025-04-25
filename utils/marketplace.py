import pandas as pd

def fetch_marketplace_data():
    # Load marketplace data
    data = pd.read_csv('data/market_demand.csv')
    return data.to_dict(orient='records')
