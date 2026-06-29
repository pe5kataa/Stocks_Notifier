from ingestion.stocks_extract import extract_prices, extract_prices
from ingestion.stocks_load import load_stock_prices


def run():
    tickers = ["AAPL", "MSFT", "NVDA", "TSLA"]
    df = extract_prices(tickers, '2026-01-01', '2026-06-24')
    load_stock_prices(df)
    
if __name__ == "__main__":
    run()