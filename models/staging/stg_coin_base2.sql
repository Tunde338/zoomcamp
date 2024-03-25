-- CREATE OR REPLACE TABLE `latest-project-410306.dbt_jtunde.stg_bcoin_table`
-- OPTIONS()
-- AS
SELECT * FROM {{ source ('data_talk_final_project', 'data_talk_final_project_table') }}
