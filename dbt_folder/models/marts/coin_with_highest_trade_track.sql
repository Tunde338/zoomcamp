SELECT
    fmd.baseId,
    dc.quoteId,
    AVG(fmd.volumeUsd24Hr) AS average_usd_in_24hr
FROM
    {{ ref('fact_market_data') }} AS fmd
JOIN
    {{ ref('dim_currency') }} AS dc
ON
    fmd.baseId = dc.baseId
GROUP BY
    fmd.baseId, dc.quoteId
ORDER BY
    average_usd_in_24hr DESC
