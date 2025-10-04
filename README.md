# OptionsDataAnalyzer

This project is a Python-based tool designed to fetch, clean, and analyze stock options data from the Polygon.io API. The primary goal is to build a foundational data pipeline that can be used for more complex trading strategies in the future, including AI-driven analysis.

Currently, the software successfully connects to the API, fetches the entire options chain for a given stock and expiration date, cleans the nested data returned by the API, and performs an initial analysis by filtering the hundreds of available options down to a manageable list of contracts near the current stock price.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone the Repository
2. Set up the Python Environment
3. Install Dependencies
4. Add Your API Key
5. Run the Main Script

Instructions for using the software:

1. The script is currently hard-coded to analyze the SPY ticker for a specific expiration date
2. Simply run the main.py file as instructed above
3. The output will be printed to the console, showing the total number of options contracts found and how many are left after the filter is applied, along with their strike price range.

## Development Environment

To recreate the development environment, you need the following software and libraries:

- Python (Version 3.9+)
- Pandas (for data manipulation)
- polygon-io-client (for connecting to the Polygon.io API)
- python-dotenv (for securely managing the API key)

## Useful Websites to Learn More

I found these websites useful in developing this software:

- [Polygon.io API Documentation](https://polygon.io/docs)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [python-dotenv on PyPI](https://pypi.org/project/python-dotenv/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

- [ ] Implement the Sort Tool: Add a function to sort the filtered options by liquidity (open interest and volume) to find the most active contracts.
- [ ] Implement the Aggregate Tool: Add a function to calculate summary statistics, like the Put/Call Ratio, to gauge market sentiment.
- [ ] Add User Inputs: Modify the main.py script to allow the user to enter any stock ticker and expiration date instead of using hard-coded values.
- [ ] Add Data Visualization: Implement the original stretch goal to plot a chart, such as the "Volatility Smile," using Matplotlib.
