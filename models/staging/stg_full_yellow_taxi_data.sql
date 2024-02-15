select *
from
    {{ source("homework4", "full_yellow_taxi_data") }}

  