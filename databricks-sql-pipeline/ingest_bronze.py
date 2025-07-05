from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType
from datetime import date

spark = SparkSession.builder.appName("BronzeIngest").getOrCreate()

data = [
    ("S001", "C101", "Laptop", 2, 800.00, date(2024, 7, 1)),
    ("S002", "C102", "Phone", 1, 500.00, date(2024, 7, 2)),
    ("S003", "C103", "Tablet", 3, 300.00, date(2024, 7, 3))
]

schema = StructType([
    StructField("sale_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("product", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("sale_date", DateType(), True)
])

df = spark.createDataFrame(data, schema=schema)

df.write.mode("append").format("delta").saveAsTable("dev.bronze.sales_bronze")
print("✅ Data loaded to dev.bronze.sales_bronze")