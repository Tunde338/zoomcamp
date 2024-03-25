SELECT
    fmd.baseId,
    AVG(fmd.priceQuote) AS average_priceQuote
FROM
    {{ ref('fact_market_data') }} AS fmd
JOIN
    {{ ref('dim_exchange') }} AS dc
ON
    fmd.baseId = dc.baseId
GROUP BY
    fmd.baseId
ORDER BY
    average_priceQuote DESC
