from ingestion.stocks_extract import extract_prices, extract_daily_prices
from ingestion.stocks_load import load_stock_prices

tickers = ["AAPL", "MSFT", "NVDA", "TSLA"]

df = extract_daily_prices(tickers)
load_stock_prices(df)