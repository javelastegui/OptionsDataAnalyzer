import os
from dotenv import load_dotenv
from polygon import RESTClient

from data_handler import get_options_chain
from analysis_engine import filter_options

load_dotenv()
api_key = os.getenv("POLYGON_API_KEY")
client = RESTClient(api_key)

df = get_options_chain("SPY", "2025-10-06")

print("DataFrame Columns:", df.columns)

agg_response = client.get_previous_close_agg(ticker="SPY")

current_price = agg_response[0].close
print(f"SPY previous close price is: {current_price}")

print("Filtering options")
filtered_df = filter_options(df, current_price)

print(f"Original options: {len(df)}, Filtered options: {len(filtered_df)}")
print(f"Filtered Strike Range: {filtered_df['strike'].min()} to {filtered_df['strike'].max()}")