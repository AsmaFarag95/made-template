import pandas as pd
 
# Source URL
source_url =   "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"


# Read CSV data into a DataFrame
df = pd.read_csv(source_url, delimiter=";")

 
# Define SQLite data types for each column
sqlite_data_types = {
    "column_1": "INTEGER",
    "column_2": "TEXT",
    "column_3": "TEXT",
    "column_4": "TEXT",
    "column_5": "TEXT",
    "column_6": "TEXT",
    "column_7": "REAL",
    "column_8": "REAL",
    "column_9": "INTEGER",
    "column_10": "REAL",
    "column_11": "TEXT",
    "column_12": "TEXT",
    "geo_punkt": "TEXT",
}


# Create the SQLite table
df.to_sql("airports", "sqlite:///airports.sqlite" , if_exists="replace", index=False , dtype = sqlite_data_types)

# Confirm the successful creation of the table
print("Table 'airports' created successfully.")
