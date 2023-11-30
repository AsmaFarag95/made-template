import pandas as pd
<<<<<<< HEAD
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
=======
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
engine = create_engine("sqlite:///airports.sqlite")

# Create the SQLite table, the content of the DataFrame df is written  into a table named "airports" in the SQLite database
#using the specified SQLite data types (sqlite_data_types).
df.to_sql("airports", con=engine, if_exists="replace", index=False, dtype=sqlite_data_types)

 
>>>>>>> origin/main
