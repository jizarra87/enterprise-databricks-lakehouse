from faker import Faker
import pandas as pd
import random
from datetime import datetime

fake = Faker()

NUM_RECORDS = 10
START_ORDER_ID = 6000

orders = []

for order_id in range(START_ORDER_ID, START_ORDER_ID + NUM_RECORDS):

    customer_id = random.randint(1, 1000)

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
    "C:\Users\juanc\enterprise-databricks-lakehouse\data\raw\orders_stream_batch2.csv",
    index=False
)

print(f"{NUM_RECORDS} streaming records generated.")