from data_handler import get_options_chain

# implied_volatility greeks open_interest strike_price option_type volume

def filter_options(df, stock_price, range_percent=0.05):
    min_strike = stock_price * (1 - range_percent)
    max_strike = stock_price * (1 + range_percent)

    return df[(df['strike'] >= min_strike) & (df['strike'] <= max_strike)]
