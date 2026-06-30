with metrics as (SELECT ticker,
    date,
    close,
    close - LAG(close) OVER (PARTITION BY ticker ORDER BY date) as price_change,
    close / LAG(close) OVER (PARTITION BY ticker ORDER BY date) - 1 as daily_return
FROM {{ ref('stg_stock_prices') }})

SELECT *
FROM metrics
WHERE date = (SELECT MAX(date) FROM metrics)