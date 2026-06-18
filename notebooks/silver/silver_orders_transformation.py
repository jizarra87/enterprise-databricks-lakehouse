# Databricks notebook source
from pyspark.sql.functions import col
from pyspark.sql.types import LongType

bronze_orders_df = spark.table("enterprise_lakehouse.bronze.orders")

silver_orders_df = (
    bronze_orders_df
    .withColumn("order_id", col("order_id").cast(LongType()))
    .dropDuplicates(["order_id"])
    .filter(col("total_amount") > 0)
    .filter(col("quantity") > 0)
)

silver_orders_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("enterprise_lakehouse.silver.orders")