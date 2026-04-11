from google.cloud import bigquery
import pandas as pd

# 1. Tell the client exactly which project to use
client = bigquery.Client(project='bigquery-public-data-491918')

# 2. Update your query with the actual table path
# I'm using a standard public dataset table here so you can test if it works
query = """
    SELECT * FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`
    LIMIT 10
"""

try:
    # 3. Run the query
    df = client.query(query).to_dataframe()
    print(df)
except Exception as e:
    print(f"Error: {e}")