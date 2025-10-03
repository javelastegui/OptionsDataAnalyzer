import os
import pandas as pd
from dotenv import load_dotenv
from polygon import RESTClient

load_dotenv()

api_key = os.getenv("POLYGON_API_KEY")
client = RESTClient(api_key)

def get_options_chain(ticker: str, expiry_date: str):
    raw_data = list(client.list_snapshot_options_chain(
        ticker,
        params={
            "expiration_date": expiry_date,
        }
    ))

    df = pd.DataFrame(raw_data)
    return df

spy_df = get_options_chain("SPY", "2025-10-03")