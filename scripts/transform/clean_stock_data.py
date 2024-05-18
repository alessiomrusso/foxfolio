import pandas as pd

def clean_instrument_data(instrument_data):
    info = instrument_data.info
    historical_data = instrument_data.history(period="1y")
    df = pd.DataFrame(historical_data)
    open_data_by_date = pd.DataFrame(df['Open'].items(), columns=['Date', 'Open'])
    close_data_by_date = pd.DataFrame(df['Close'].items(), columns=['Date', 'Close'])
    cleaned_historical_data = pd.merge(open_data_by_date, close_data_by_date, on='Date', how='inner')
    cleaned_historical_data['Symbol'] = info['symbol']
    cleaned_historical_data['Date'] = pd.to_datetime(cleaned_historical_data['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')
    return cleaned_historical_data
