SELECT * FROM {{ source('homework4', 'full_yellow_taxi_data') }}



-- -- Selecting columns from the source table
-- SELECT
--     vendorid,
--     lpep_pickup_datetime,
--     lpep_dropoff_datetime,
--     store_and_fwd_flag,
--     ratecodeid, -- Enclosed in backticks to handle the space
--     pulocationid,
--     dolocationid,
--     passenger_count,
--     trip_distance,
--     fare_amount,
--     extra,
--     mta_tax,
--     tip_amount,
--     tolls_amount,
--     ehail_fee,
--     improvement_surcharge,
--     total_amount,
--     payment_type,
--     trip_type,
--     congestion_surcharge
-- FROM source
