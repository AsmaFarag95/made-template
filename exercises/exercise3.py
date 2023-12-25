import pandas as pd
import sqlite3

# Step 1: Download and Read the CSV
url= "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv";
df = pd.read_csv(url, encoding=" latin-1", delimiter=";", skiprows=6, skipfooter=4) #skip meta data

#df = pd.read_csv(url, encoding='cp1252')


print(df.columns)

# Define mapping for column names
column_mapping = {
    'Unnamed: 0': 'date',
    'Unnamed: 1': 'CIN',
    'Unnamed: 2': 'name',
    'Insgesamt': 'petrol',
    'Insgesamt.1': 'diesel',
    'Insgesamt.2': 'gas',
    'Insgesamt.3': 'electro',
    'Insgesamt.4': 'hybrid',
    'Insgesamt.5': 'plugInHybrid',
    'Insgesamt.6': 'others'
}


# Rename columns based on the mapping
df.rename(columns=column_mapping, inplace=True)

new_df = df[['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']]



 
# Validate CINs
new_df["CIN"] = new_df["CIN"].astype(str).str.zfill(5)


# Validate numeric columns
numeric_columns = ["petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]
new_df[numeric_columns] = new_df[numeric_columns].apply(pd.to_numeric, errors="coerce") #If ‘coerce’, then invalid parsing will be set as NaN
new_df = new_df.dropna()  # Drop rows with invalid values


#   Use fitting SQLite types
sqlite_types = {"date": "TEXT", "CIN": "TEXT", "name": "TEXT", **{col: "INTEGER" for col in numeric_columns}}

# Step 5: Write to SQLite Database
conn = sqlite3.connect("cars.sqlite")
new_df.to_sql("cars", conn, if_exists="replace", index=False, dtype=sqlite_types)
conn.close()
