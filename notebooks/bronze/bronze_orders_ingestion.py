from pyspark.sql.functions import current_timestamp, lit, col

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