# Databricks notebook source
from pyspark.sql.functions import upper, trim, col

bronze_df = spark.table("enterprise_lakehouse.bronze.customers")

silver_df = (
    bronze_df
    .dropDuplicates(["customer_id"])
    .withColumn("first_name", trim(col("first_name")))
    .withColumn("last_name", trim(col("last_name")))
    .withColumn("email", trim(col("email")))
    .withColumn("country", upper(col("country")))
)

display(silver_df)

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("enterprise_lakehouse.silver.customers")

# COMMAND ----------

 