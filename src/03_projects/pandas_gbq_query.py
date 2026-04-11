import pandas as pd

print(pd.read_gbq("SELECT * FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` LIMIT 10", project_id='bigquery-public-data-491918'))