# Databricks notebook source
from pyspark.sql.functions import current_timestamp, lit

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/raw/customers.csv")
)

bronze_df = (
    df.withColumn("ingestion_timestamp", current_timestamp())
      .withColumn("source_system", lit("crm"))
      .withColumn("ingestion_layer", lit("bronze"))
)

display(bronze_df)

bronze_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("enterprise_lakehouse.bronze.customers")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.default.bronze_customers
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY workspace.default.bronze_customers

# COMMAND ----------

