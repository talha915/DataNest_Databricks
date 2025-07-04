import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run_sql import run_query_file

def test_bronze_customer_data_exists():
    result = run_query_file("sql/bronze/check_customer_data.sql")
    assert result[0][0] > 0  # Check ke bronze table mein data maujood hai
