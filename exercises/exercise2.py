import pandas as pd
from sqlalchemy import create_engine

# Define the CSV link
csv_link = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
 

# Define SQLite database and table names
SQLdb_name = "trainstops.sqlite"
table_name = "trainstops"

# Read the CSV into a pandas DataFrame
df = pd.read_csv(csv_link, delimiter=";")

# Drop the "Status" column
df = df.drop("Status", axis=1) #last clm # (axis=1 Means we want to operate on clms).

# Define a function to check and clean values
def clean_values(value):
    if pd.isnull(value):
        return False
    return True

# Apply the clean_values function to each relevant column
columns_to_clean = ["Verkehr", "Laenge", "Breite", "IFOPT"]
for column in columns_to_clean:
    df = df[df[column].apply(clean_values)]

# Filter rows based on "Verkehr" values
valid_verkehr_values = ["FV", "RV", "nur DPN"]
df = df[df["Verkehr"].isin(valid_verkehr_values)]

# Filter rows based on "Laenge" and "Breite" values
df = df[(df["Laenge"] >= -90) & (df["Laenge"] <= 90) & (df["Breite"] >= -90) & (df["Breite"] <= 90)]

# Filter rows based on the IFOPT pattern
#IFOPT, or Identifikationscode für ÖPNV-Teilnehmer (Identification of Fixed Objects in Public Transport), 
ifo_pattern = r'^[a-zA-Z]{2}:\d+:\d+(:\d+)?$'
df = df[df["IFOPT"].str.match(ifo_pattern)]

# Define SQLite types for each column
sqlite_types = {
    "EVA_NR": "BIGINT",
    "DS100": "TEXT",
    "IFOPT": "TEXT",
    "NAME": "TEXT",
    "Verkehr": "TEXT",
    "Laenge": "FLOAT",
    "Breite": "FLOAT",
    "Betreiber_Name": "TEXT",
    "Betreiber_Nr": "TEXT",
}

# Create an SQLite engine and write the DataFrame to the database
engine = create_engine(f"sqlite:///{SQLdb_name}")
df.to_sql(table_name, engine, index=False, if_exists="replace", dtype=sqlite_types)
