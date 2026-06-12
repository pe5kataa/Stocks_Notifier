from airflow.decorators import dag, task
from datetime import datetime, timedelta
import sys

MARKET_INTEL_PY = "/opt/miniconda3/envs/market-intel/bin/python"


@dag(dag_id="daily_stock_upload",start_date=datetime(2026, 1, 1), schedule="@daily", catchup=False)
def run_daily_price_pipeline():
    
    @task.external_python(python=MARKET_INTEL_PY, retries = 20, retry_delay=timedelta(seconds=10))
    def extract():
        from ingestion.stocks_extract import extract_daily_prices
        tickers = ["AAPL", "MSFT", "NVDA", "TSLA"]
        df = extract_daily_prices(tickers)
        if df.empty:
            print("NO MARKET DATA TODAY")
            sys.exit(99) 
        df.to_csv("/tmp/stocks.csv", index=False)
        return "/tmp/stocks.csv" 

    @task.external_python(python=MARKET_INTEL_PY)
    def load(path):
        from ingestion.stocks_load import load_stock_prices
        import pandas as pd
        df = pd.read_csv(path)
        load_stock_prices(df)
        
    load(extract())
    
run_daily_price_pipeline()