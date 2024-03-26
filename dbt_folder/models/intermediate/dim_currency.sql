SELECT
    baseId, 
    baseSymbol, 
    quoteId, 
    quoteSymbol 
FROM {{ ref('stg_coin_base2') }}
