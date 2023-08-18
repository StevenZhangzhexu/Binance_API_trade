from binance.client import Client
import os
import pandas as pd


def get_history(symbol, interval, start, end = None):
    bars = client.get_historical_klines(symbol = symbol, interval = interval,
                                        start_str = start, end_str = end, limit = 1000)
    df = pd.DataFrame(bars)
    df["Date"] = pd.to_datetime(df.iloc[:,0], unit = "ms")
    df.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume",
                  "Clos Time", "Quote Asset Volume", "Number of Trades",
                  "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore", "Date"]
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
    df.set_index("Date", inplace = True)
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors = "coerce")
    
    return df

if __name__ == "__main__": 
    api_key = os.environ["BINANCE_API_KEY"]
    secret_key = os.environ["BINANCE_SECRET"]
    client = Client(api_key = api_key, api_secret = secret_key, tld = "com")

    df = get_history(symbol = "BTCUSDT", interval = "1h",
                 start = "2020-01-01 10:00:00", end = "2022-12-31 23:59:59")