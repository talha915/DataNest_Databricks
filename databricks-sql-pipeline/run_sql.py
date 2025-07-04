from databricks import sql
from config import DATABRICKS_HOST, HTTP_PATH, ACCESS_TOKEN

def run_query_file(file_path: str):
    with open(file_path, "r") as f:
        query = f.read()

    with sql.connect(
        server_hostname=DATABRICKS_HOST,
        http_path=HTTP_PATH,
        access_token=ACCESS_TOKEN
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            try:
                return cursor.fetchall()
            except:
                return None
