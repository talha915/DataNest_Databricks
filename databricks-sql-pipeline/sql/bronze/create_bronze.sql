CREATE OR REPLACE TABLE dev.bronze.sales_bronze (
    sale_id STRING,
    customer_id STRING,
    product STRING,
    quantity INT,
    price DOUBLE,
    sale_date DATE
)
USING DELTA
TBLPROPERTIES ("quality" = "bronze");


