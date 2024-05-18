import yfinance as yf
import pandas as pd

def fetch_stock_historical_data(ticker):
    instrument_data = yf.Ticker(ticker)
    return instrument_data