SELECT
    de.baseId,
    fmd.rank,
    dc.baseSymbol
FROM
    {{ ref('fact_market_data') }} AS fmd
JOIN
    {{ ref('dim_exchange') }} AS de
ON
    fmd.baseId = de.baseId
JOIN
    {{ ref('dim_currency') }} AS dc
ON
    dc.baseId = de.baseId
GROUP BY
    de.baseId,
    fmd.rank,
    dc.baseSymbol
ORDER BY
    fmd.rank DESC