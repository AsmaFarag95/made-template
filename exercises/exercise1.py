import pandas as pd
 
from sqlalchemy import create_engine, Integer, Text, Float #create_engine is a function from sqlalchemy used to create a connection to the SQLite database.

# Read CSV data into a DataFrame,  This DataFrame is  a dataset that holds the tabular data from the CSV file.
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
engine = create_engine("sqlite:///data/airports.sqlite")
print("done")
# Create the SQLite table, the content of the DataFrame df is written  into a table named "airports" in the SQLite database
#using the specified SQLite data types (sqlite_data_types).
df.to_sql("airports", con=engine, if_exists="replace", index=False, dtype=sqlite_data_types)

 
 