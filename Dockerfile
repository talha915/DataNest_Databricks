# Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY databricks-sql-pipeline ./databricks-sql-pipeline

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["pytest", "tests/"]

CMD [ "bash" ]
