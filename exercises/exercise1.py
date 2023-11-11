import pandas as pd
 
# Source URL
source_url =   "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"


# Read CSV data into a DataFrame
df = pd.read_csv(source_url, delimiter=";")

 
# Define SQLite data types for each column
sqlite_data_types = {
    "column_1": types.INTEGER,
    "column_2": types.TEXT,
    "column_3": types.TEXT,
    "column_4": types.TEXT,
    "column_5": types.TEXT,
    "column_6": types.TEXT,
    "column_7": types.FLOAT,
    "column_8": types.FLOAT,
    "column_9": types.INTEGER,
    "column_10": types.FLOAT,
    "column_11": types.TEXT,
    "column_12": types.TEXT,
    "geo_punkt": types.TEXT,
}

# Create the SQLite table
df.to_sql("airports", "sqlite:///airports.sqlite" , if_exists="replace", index=False)

# Confirm the successful creation of the table
print("Table 'airports' created successfully.")
