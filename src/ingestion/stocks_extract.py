import requests
from datetime import date
import pandas as pd
import yfinance as yf

def extract_prices(list:list):
    end_date = date.today().isoformat()
    data = yf.download(
        list, 
        start="2020-01-01", 
        end=end_date,
        group_by='ticker'
    )
    dfs = []
    for ticker in list:
        ticker_df = data[ticker]
        ticker_df["Ticker"] = ticker
        dfs.append(ticker_df)
    
    final_df = pd.concat(dfs)
    final_df = final_df.reset_index()
            
    return final_df

tickers = ["AAPL", "MSFT", "NVDA", "TSLA"]
data = extract_prices(tickers)
print(data)
data.to_csv("stocks.csv")

