import dlt

from pyspark.sql.functions import (
    current_timestamp,
    lit,
    col
)

@dlt.table(
    name="orders_bronze",
    comment="Bronze orders table ingested from raw CSV files."
)
def orders_bronze():

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv("/Volumes/workspace/default/raw/orders.csv")
    )

    df = (
        df
        .withColumn("order_id", col("order_id").cast("long"))
        .withColumn("customer_id", col("customer_id").cast("long"))
        .withColumn("quantity", col("quantity").cast("integer"))
        .withColumn("unit_price", col("unit_price").cast("double"))
        .withColumn("total_amount", col("total_amount").cast("double"))
    )

    return (
        df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("source_system", lit("ecommerce"))
        .withColumn("ingestion_layer", lit("bronze"))
    )

@dlt.table(
    name="orders_silver",
    comment="Validated orders table."
)
@dlt.expect_or_drop(
    "valid_order_id",
    "order_id IS NOT NULL"
)
@dlt.expect_or_drop(
    "valid_customer_id",
    "customer_id IS NOT NULL"
)
@dlt.expect_or_drop(
    "positive_quantity",
    "quantity > 0"
)
@dlt.expect_or_drop(
    "positive_amount",
    "total_amount > 0"
)
def orders_silver():

    return dlt.read("orders_bronze")