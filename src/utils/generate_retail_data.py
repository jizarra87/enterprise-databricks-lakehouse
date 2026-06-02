from faker import Faker
import pandas as pd
import random
from datetime import datetime

fake = Faker()

NUM_CUSTOMERS = 1000

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    customers.append({
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.state(),
        "country": "USA",
        "created_at": datetime.now()
    })

df_customers = pd.DataFrame(customers)

df_customers.to_csv(
    "data/raw/customers.csv",
    index=False
)

print("Customer dataset generated successfully.")

NUM_ORDERS = 5100

orders = []

for order_id in range(1, NUM_ORDERS + 1):

    customer_id = random.randint(1, NUM_CUSTOMERS)

    quantity = random.randint(1, 5)

    unit_price = round(random.uniform(10, 500), 2)

    total_amount = round(quantity * unit_price, 2)

    orders.append({
        "order_id": order_id,
        "customer_id": customer_id,
        "order_date": fake.date_this_year(),
        "quantity": quantity,
        "unit_price": unit_price,
        "total_amount": total_amount,
        "created_at": datetime.now()
    })

df_orders = pd.DataFrame(orders)

df_orders.to_csv(
    "data/raw/orders.csv",
    index=False
)

print("Orders dataset generated successfully.")