{{ config(materialized='table') }}

select
    o.order_id,
    o.customer_id,
    o.order_date,
    year(o.order_date) as order_year,
    month(o.order_date) as order_month,
    o.quantity,
    o.unit_price,
    o.total_amount,
    c.city,
    c.state,
    c.country
from enterprise_lakehouse.silver.orders o
join enterprise_lakehouse.silver.customers c
    on o.customer_id = c.customer_id