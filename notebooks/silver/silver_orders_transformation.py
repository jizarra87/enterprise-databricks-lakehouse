# Databricks notebook source
from pyspark.sql.functions import col

bronze_orders_df = spark.table("enterprise_lakehouse.bronze.orders")

silver_orders_df = (
    bronze_orders_df
    .dropDuplicates(["order_id"])
    .filter(col("total_amount") > 0)
    .filter(col("quantity") > 0)
)

display(silver_orders_df)
silver_orders_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("enterprise_lakehouse.silver.orders")