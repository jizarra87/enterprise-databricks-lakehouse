{{ config(materialized='table') }}

select
    customer_id,
    first_name,
    last_name,
    email,
    city,
    state,
    country,
    created_at
from enterprise_lakehouse.silver.customers