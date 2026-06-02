# Databricks notebook source
from pyspark.sql.functions import (
    col,
    year,
    month
)

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

display(fact_sales_df)

fact_sales_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("enterprise_lakehouse.gold.fact_sales")