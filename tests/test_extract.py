import pandas as pd
from unittest.mock import patch
from ingestion.stocks_extract import extract_prices

@patch("ingestion.stocks_extract.yf.download")
def test_extract_prices(mock_download):
    
    tickers = ["AAPL", "MSFT", "NVDA", "TSLA"] 
    
    df = pd.DataFrame(
        {
            ("AAPL", "Close"): [100],
            ("MSFT", "Close"): [100],
            ("NVDA", "Close"): [100],
            ("TSLA", "Close"): [100],
        },
        index=pd.to_datetime(["2026-01-01"]),
    )
    
    mock_download.return_value = df
    
    result = extract_prices(tickers, "2026-01-01", "2026-01-02")
    
    assert "Ticker" in result.columns
    assert set(result["Ticker"]) == {"AAPL", "MSFT", "NVDA", "TSLA"}