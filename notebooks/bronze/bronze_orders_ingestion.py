# Databricks notebook source
from pyspark.sql.functions import current_timestamp, lit

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/raw/orders.csv")
)

bronze_df = (
    df.withColumn("ingestion_timestamp", current_timestamp())
      .withColumn("source_system", lit("ecommerce"))
      .withColumn("ingestion_layer", lit("bronze"))
)

display(bronze_df)

bronze_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("enterprise_lakehouse.bronze.orders")