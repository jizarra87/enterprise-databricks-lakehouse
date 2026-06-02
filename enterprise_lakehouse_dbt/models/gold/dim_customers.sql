select
    customer_id,
    first_name,
    last_name,
    email,
    city,
    state,
    country,
    created_at

from read_csv_auto('../data/raw/customers.csv')