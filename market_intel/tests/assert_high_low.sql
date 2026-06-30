SELECT high, low
FROM {{ ref('stg_stock_prices') }}
WHERE high < low