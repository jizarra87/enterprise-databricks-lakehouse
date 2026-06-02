from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit
import os

os.environ["HADOOP_HOME"] = "C:\\hadoop"
os.environ["PYSPARK_PYTHON"] = "python"


spark = (
    SparkSession.builder
    .appName("bronze-customers-ingestion")
    .getOrCreate()
)

source_path = "data/raw/customers.csv"
target_path = "data/bronze/customers"

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(target_path)
)

bronze_df = (
    df.withColumn("ingestion_timestamp", current_timestamp())
      .withColumn("source_system", lit("crm"))
      .withColumn("ingestion_layer", lit("bronze"))
)

(
    bronze_df.write
            .mode("overwrite")
            .option("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")
            .parquet(target_path)
)

print("Bronze customers ingestion completed successfully.")

spark.stop()