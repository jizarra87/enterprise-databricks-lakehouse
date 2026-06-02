# Databricks notebook source
from pyspark.sql.functions import (
    current_timestamp,
    lit,
    col
)

new_orders_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/raw/orders.csv")
)

bronze_incremental_df = (
    new_orders_df
    .withColumn("ingestion_timestamp", current_timestamp())
    .withColumn("source_system", lit("ecommerce"))
    .withColumn("ingestion_layer", lit("bronze"))
)

bronze_incremental_df.createOrReplaceTempView("incoming_orders")

merge_sql = """
MERGE INTO enterprise_lakehouse.silver.orders AS target
USING incoming_orders AS source
ON target.order_id = source.order_id

WHEN MATCHED THEN
UPDATE SET
    target.customer_id = source.customer_id,
    target.order_date = source.order_date,
    target.quantity = source.quantity,
    target.unit_price = source.unit_price,
    target.total_amount = source.total_amount,
    target.created_at = source.created_at,
    target.ingestion_timestamp = source.ingestion_timestamp

WHEN NOT MATCHED THEN
INSERT *
"""

spark.sql(merge_sql)

print("Incremental MERGE completed successfully.")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT COUNT(*)
# MAGIC FROM enterprise_lakehouse.silver.orders