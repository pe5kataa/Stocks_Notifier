SELECT date
FROM {{ ref('stg_stock_prices') }}
GROUP BY date
HAVING COUNT(DISTINCT ticker) < 4