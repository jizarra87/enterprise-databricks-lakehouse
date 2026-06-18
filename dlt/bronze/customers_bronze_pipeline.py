import dlt
from pyspark.sql.functions import upper, trim, col
from pyspark.sql.functions import (
    current_timestamp,
    lit,
    col
)

@dlt.table(
        name="customers",
        comment="Bronze customers table ingested from raw CSV files"
)

def customers_bronze():
    df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/raw/customers.csv")
    )

    return (
        df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("source_system", lit("ecommerce"))
        .withColumn("ingestion_layer", lit("bronze"))
    )