from database.connection import engine
from sqlalchemy.dialects.postgresql import insert


def _insert_on_conflict_nothing(table, conn, keys, data_iter):
    """Append rows but skip any that violate the primary key (idempotent load)."""
    data = [dict(zip(keys, row)) for row in data_iter]
    stmt = insert(table.table).values(data).on_conflict_do_nothing()
    result = conn.execute(stmt)
    
    attempted = len(data)
    inserted = result.rowcount
    skipped = attempted - inserted
    
    print(f"Load: attempted {attempted} | inserted {inserted} | skipped {skipped} (duplicates)")
    return result.rowcount


def load_stock_prices(df):
    df.to_sql(
        "raw_stock_prices",
        con=engine,
        schema="raw",
        if_exists="append",
        index=False,
        method=_insert_on_conflict_nothing,
    )