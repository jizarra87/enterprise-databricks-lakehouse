import dlt

from pyspark.sql.functions import trim, upper, col

@dlt.table(
    name="customers",
    comment="Silver customers table with deduplicated and standardized customer records."
)
@dlt.expect_all_or_drop({
    "valid_customer_id": "customer_id IS NOT NULL",
    "valid_email": "email IS NOT NULL"
})
def customers():
    return (
        spark.read.table("enterprise_lakehouse_dev.bronze.customers")
        .dropDuplicates(["customer_id"])
        .withColumn("first_name", trim(col("first_name")))
        .withColumn("last_name", trim(col("last_name")))
        .withColumn("email", trim(col("email")))
        .withColumn("country", upper(col("country")))
    )


@dlt.table(
    name="customers_quarantine",
    comment="Rejected customer records that failed validation rules."
)
def customers_quarantine():
    return (
        spark.read.table("enterprise_lakehouse_dev.bronze.customers")
        .filter(
            """
            customer_id IS NULL
            OR email IS NULL
            """
        )
    )