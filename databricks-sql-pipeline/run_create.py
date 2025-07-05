from run_sql import run_query_file

if __name__ == "__main__":
    run_query_file("sql/bronze/create_bronze.sql")
    print("✅ Table created")

    run_query_file("sql/bronze/insert_bronze.sql")
    print("✅ Sample data inserted")
