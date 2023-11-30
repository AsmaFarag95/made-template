import pandas as pd
from sqlalchemy import create_engine, Integer, Text, Float
 
# Read CSV data into a DataFrame
df = pd.read_csv("https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv", delimiter=";")

# Define SQLite data types for each column
sqlite_data_types = {
    "column_1": Integer(),
    "column_2": Text(),
    "column_3": Text(),
    "column_4": Text(),
    "column_5": Text(),
    "column_6": Text(),
    "column_7": Float(),
    "column_8": Float(),
    "column_9": Integer(),
    "column_10": Float(),
    "column_11": Text(),
    "column_12": Text(),
    "geo_punkt": Text(),
}

# Create SQLite database engine
engine = create_engine("sqlite:///PYairports.sqlite" , echo=True)

# Create the SQLite table
df.to_sql("PYairports", con=engine, if_exists="replace", index=False, dtype=sqlite_data_types)

# Confirm the successful creation of the table
print("Table 'airports' created successfully.")
