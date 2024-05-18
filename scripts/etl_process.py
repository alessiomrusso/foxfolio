from scripts.extract.fetch_stock_data import fetch_stock_historical_data
from scripts.transform.clean_stock_data import clean_instrument_data
from scripts.load.load_to_db2 import load_data
import configparser

def etl_process(ticker):
    # Extract data from source
    instrument_data = fetch_stock_historical_data(ticker)
    
    # Transform data
    stock_performances_data = clean_instrument_data(instrument_data)
    
    # Load to DB
    load_data(stock_performances_data, "STOCKS")
