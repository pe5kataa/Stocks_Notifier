from sqlalchemy import (
    MetaData, Table, Column, String, Date, Numeric, TIMESTAMP, text
)
from database.connection import engine

metadata = MetaData(schema="raw")

# Columns mirror exactly what extract_prices() returns (faithful raw layer).
stock_prices = Table(
    "raw_stock_prices", metadata,
    Column("Ticker", String, primary_key=True),
    Column("Date", Date, primary_key=True),
    Column("Open", Numeric),
    Column("High", Numeric),
    Column("Low", Numeric),
    Column("Close", Numeric),
    Column("Adj Close", Numeric),
    Column("Volume", Numeric),
    Column("loaded_at", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
)

if __name__ == "__main__":
    metadata.create_all(engine)
