import sys
import os

# Add parent directory for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run_sql import run_query_file

# Compute absolute paths for SQL files relative to this test file
SQL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql', 'bronze'))

def test_bronze_customer_data_exists():
    sql_file = os.path.join(SQL_DIR, "check_customer_data.sql")
    result = run_query_file(sql_file)
    assert result[0][0] > 0  

def test_bronze_customer_data_count():
    sql_file = os.path.join(SQL_DIR, "check_customer_data.sql")
    result = run_query_file(sql_file)
    count = result[0][0]
    assert count >= 75000, f"Expected at least 75000 records, but got {count}"

def test_sales_table_exists():
    sql_file = os.path.join(SQL_DIR, "check_bronze.sql")
    result = run_query_file(sql_file)
    assert result[0][0] == 1, "❌ sales_bronze table does not exist"
