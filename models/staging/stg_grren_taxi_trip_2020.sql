WITH source AS (
    SELECT * FROM {{ source('ny_taxi', 'grren_taxi_trip_2020') }}
)

-- Selecting columns from the source table
SELECT
    {{ dbt_utils.generate_surrogate_key(['vendorid', 'lpep_pickup_datetime']) }} as tripid,
    vendorid,
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    store_and_fwd_flag,
    ratecodeid, -- Enclosed in backticks to handle the space
    pulocationid,
    dolocationid,
    passenger_count,
    trip_distance,
    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    ehail_fee,
    improvement_surcharge,
    total_amount,
    payment_type,
    {{ get_payment_type_description('payment_type') }} as payment_type_description,
    trip_type,
    congestion_surcharge
FROM source

