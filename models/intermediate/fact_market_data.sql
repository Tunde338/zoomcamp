SELECT
    priceQuote, 
    rank, 
    priceUsd, 
    volumeUsd24Hr,
    percentExchangeVolume,
    tradesCount24Hr  
FROM {{ ref('stg_coin_base2') }}
