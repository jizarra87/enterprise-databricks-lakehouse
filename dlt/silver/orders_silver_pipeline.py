import dlt

@dlt.table(
    name="orders",
    comment="Silver orders table with validated order records."
)
@dlt.expect_all_or_drop({
    "valid_order_id": "order_id IS NOT NULL",
    "valid_customer_id": "customer_id IS NOT NULL",
    "positive_quantity": "quantity > 0",
    "positive_amount": "total_amount > 0"
})
def orders():
    return spark.read.table("enterprise_lakehouse_dev.bronze.orders")


@dlt.table(
    name="orders_quarantine",
    comment="Rejected order records that failed validation rules."
)
def orders_quarantine():
    return (
        spark.read.table("enterprise_lakehouse_dev.bronze.orders")
        .filter(
            """
            order_id IS NULL
            OR customer_id IS NULL
            OR quantity <= 0
            OR total_amount <= 0
            """
        )
    )