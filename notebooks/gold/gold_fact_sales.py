# Databricks notebook source
from pyspark.sql.functions import (
    col,
    year,
    month
)
from pyspark.sql.types import LongType

orders_df = spark.table("enterprise_lakehouse.silver.orders")

customers_df = spark.table("enterprise_lakehouse.gold.dim_customers")

fact_sales_df = (
    orders_df.alias("o")
    .join(
        customers_df.alias("c"),
        col("o.customer_id") == col("c.customer_id"),
        "inner"
    )
    .select(
        col("o.order_id"),
        col("o.customer_id"),
        col("o.order_date"),
        year(col("o.order_date")).alias("order_year"),
        month(col("o.order_date")).alias("order_month"),
        col("o.quantity"),
        col("o.unit_price"),
        col("o.total_amount"),
        col("c.city"),
        col("c.state"),
        col("c.country")
    )
)


fact_sales_df = (
    fact_sales_df.withColumn("order_id", col("order_id").cast(LongType()))
    .withColumn("customer_id", col("customer_id").cast(LongType()))    
)


fact_sales_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("enterprise_lakehouse.gold.fact_sales")