import pandas as pd
from sqlalchemy import create_engine, Integer, Text, Float

# Read CSV data into a DataFrame
df = pd.read_csv("https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv", delimiter=";")

# Define SQLite data types for each column using a loop
sqlite_data_types = {}
for column in df.columns:
    if df[column].dtype == 'int64':
        sqlite_data_types[column] = Integer()
    elif df[column].dtype == 'float64':
        sqlite_data_types[column] = Float()
    else:
        sqlite_data_types[column] = Text()

# Create SQLite database engine
engine = create_engine("sqlite:///airports.sqlite")

# Create the SQLite table
df.to_sql("airports", con=engine, if_exists="replace", index=False, dtype=sqlite_data_types)

# Confirm the successful creation of the table
print("Table 'airports' created successfully.")
