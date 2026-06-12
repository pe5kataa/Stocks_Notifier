from datetime import date, timedelta
import pandas as pd
import yfinance as yf

def extract_prices(tickers:list, start_date:str, end_date:str):
    data = yf.download(
        tickers, 
        start= start_date, 
        end=end_date,
        group_by='ticker'
    )
    dfs = []
    for ticker in tickers:
        ticker_df = data[ticker].copy()
        ticker_df["Ticker"] = ticker
        dfs.append(ticker_df)
    
    final_df = pd.concat(dfs)
    final_df = final_df.reset_index()
            
    return final_df


def extract_daily_prices(tickers):
    today = date.today()
    start = today.isoformat()
    end = (today + timedelta(days=1)).isoformat()
    return extract_prices(tickers, start, end)