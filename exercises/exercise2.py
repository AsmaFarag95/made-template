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

# Define column data types
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

 
    
link = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
dataFrame = pd.read_csv(link, delimiter=";")
 
    # Drop the "Status" column
dataFrame.drop(columns=["Status"], inplace=True)
    
dataFrame.drop(columns=["Status"], inplace=True)

    # Filter rows with valid values
dataFrame = dataFrame[dataFrame["Verkehr"].isin(["FV", "RV", "nur DPN"])]
dataFrame['Laenge'] = pd.to_numeric(dataFrame['Laenge'].str.replace(',', '.'), errors='coerce')
dataFrame['Breite'] = pd.to_numeric(dataFrame['Breite'].str.replace(',', '.'), errors='coerce')
dataFrame = dataFrame.dropna()
dataFrame = dataFrame[~((dataFrame["Laenge"] < -90) | (dataFrame["Laenge"] > 90))]
data = dataFrame[~((dataFrame["Breite"] < -90) | (dataFrame["Breite"] > 90))]
    
dataFrame['IFOPT'] = data['IFOPT'].astype(str)
data = data[data['IFOPT'].str.match(r'^[a-zA-Z]{2}:[0-9]*:[0-9]+(:[0-9]+)?$')]
    
    
dataFrame.to_sql("trainstops", 'sqlite:///trainstops.sqlite', if_exists='replace', index=False)

 
 
