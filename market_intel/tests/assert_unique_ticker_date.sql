SELECT ticker, date, count(*)
FROM {{ ref('stg_stock_prices') }}
GROUP BY ticker, date
HAVING COUNT(*) > 1