import pandas 
 
# Source URL
source_url =   "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"


# Read CSV data into a DataFrame
df = pd.read_csv(source_url,   delimiter=";")


# Define SQLite data types for each column
sqlite_data_types = {
    "column_1": "int",
    "column_2": "str",
    "column_3": "str",
    "column_4": "str",
    "column_5": "str",
    "column_6": "str",
    "column_7": "float",
    "column_8": "float",
    "column_9": "INTEGER",
    "column_10": "int",
    "column_11": "str",
    "column_12": "str",
    "geo_punkt": "str",
}


# Create the SQLite table
df.to_sql("airportspy", "sqlite:///airportspy.sqlite" , if_exists="replace", index=False , dtype = sqlite_data_types)
print("df", df)

# Confirm the successful creation of the table
print("Table 'airports' created successfully.")
