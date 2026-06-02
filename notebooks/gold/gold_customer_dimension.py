# Databricks notebook source
from pyspark.sql.functions import upper, trim, col


gold_df = (
    spark.table("enterprise_lakehouse.silver.customers")
    .select(
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "city",
        "state",
        "country",
        "created_at"
    )
)

display(gold_df)

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("enterprise_lakehouse.gold.dim_customers")

# COMMAND ----------

