import pandas as pd

# Limpieza de los datos

col_list = ["datetime", "San Francisco"]
reader = pd.read_csv("humidity.csv", usecols=col_list)
reader = reader.rename(columns = {'San Francisco':'HUM'})
reader2 = pd.read_csv("temperature.csv", usecols=col_list)
reader2 = reader2.rename(columns = {'San Francisco':'TEMP'})

merged_inner = pd.merge(left=reader2, right=reader, left_on='datetime', right_on='datetime')
merged_inner = merged_inner.dropna()
merged_inner = merged_inner.rename(columns = {'datetime':'DATE'})

merged_inner = merged_inner.iloc[0:40]
merged_inner.to_csv('/tmp/data.csv')
