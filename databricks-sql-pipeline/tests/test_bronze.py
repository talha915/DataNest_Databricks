import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run_sql import run_query_file

def test_bronze_customer_data_exists():
    result = run_query_file("sql/bronze/check_customer_data.sql")
    assert result[0][0] > 0  


def test_bronze_customer_data_count():
    result = run_query_file("sql/bronze/check_customer_data.sql")
    count = result[0][0]
    assert count >= 75000, f"Expected at least 75000 records, but got {count}"