<<<<<<< HEAD
'''
Exercise 2
Build an automated data pipeline for the following source:
direct link to CSV: https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV

Goal

Write data into a SQLite database called “trainstops.sqlite”, in the table “trainstops”

First, drop the "Status" column

Then, drop all rows with invalid values:
Valid "Verkehr" values are "FV", "RV", "nur DPN"
Valid "Laenge", "Breite" values are geographic coordinate system values between and including -90 and 90

Valid "IFOPT" values follow this pattern:
<exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>
This is not the official IFOPT standard, please follow our guidelines and not the official standard
Empty cells are considered invalid

Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns

Allowed libraries: https://github.com/jvalue/made-exercise-feedback/blob/main/requirements.txt
 
Submit as  /exercises/exercise2.jv or  /exercises/exercise2.py depending on your language
 
'''
import pandas as pd
from sqlalchemy import create_engine

# Define the CSV link
csv_link = "/Users/asmafaraj/Downloads/D_Bahnhof_2020_alle.csv"

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
    "EVA_NR": "INT",
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
=======
import pandas as pd
types = {
            "EVA_NR": int,
            "DS100": str,
            "IFOPT": str,
            "NAME": str,
            "Verkehr": str,
            "Laenge": float,
            "Breite": float,
            "Betreiber_Name": str,
            "Betreiber_Nr": int
        }


def getDataFromLink(link):
    dataFrame = pd.read_csv(link, delimiter=";")
    return dataFrame
    


def createSQLiteFile(df):
    df.to_sql("trainstops", 'sqlite:///trainstops.sqlite',if_exists='replace', index=False)
    
    
def changeDataType(df,types):
    df = df.astype(types)
    return df
    
    
    
def cleanData(data):
    data.drop(columns=["Status"], inplace=True)
    data = data[data["Verkehr"].isin(["FV","RV","nur DPN"])]
    data.loc[:, 'Laenge'] = data['Laenge'].str.replace(',', '.')
    data.loc[:, 'Breite'] = data['Breite'].str.replace(',', '.')


    data = data.dropna()
    data = changeDataType(data,types)
    data= data[~(data["Laenge"] <= 90) & data["Laenge"] >= -90]
    data= data[~(data["Breite"] <= 90) & data["Breite"] >= -90]
    
    print(type(data['IFOPT']))
    data = data[data['IFOPT'].str.contains(r'^[a-zA-Z]{2}:[0-9]*:[0-9]+(:[0-9]+)?$')]
    data.IFOPT = data.IFOPT.astype(str)
    return data
    
def init():
    link = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
    data_frame = getDataFromLink(link)
    data_frame = cleanData(data_frame)
    createSQLiteFile(data_frame)

    
    
if __name__ == "__main__":
    init()  
>>>>>>> origin/main
