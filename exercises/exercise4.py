import pandas as pd
import zipfile
import urllib.request

types = {
        'Geraet': int,
        'Hersteller': str,
        'Model': str,
        'Monat': int,
        'Temperatur': float,
        'Batterietemperatur': float,
        'Geraet aktiv': str
        }

url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"

csv_file = "data.csv"
urllib.request.urlretrieve(url, "mowesta-dataset.zip")
with zipfile.ZipFile("mowesta-dataset.zip", 'r') as rref:
    rref.extract(csv_file)
    
file_cv =  csv_file

#Only use the columns "Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"
#Rename "Temperatur in °C (DWD)" to "Temperatur"
#Rename "Batterietemperatur in °C" to "Batterietemperatur"
 
df = pd.read_csv(file_cv, delimiter=';', index_col=False, usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])
df.columns =["Geraet", "Hersteller", "Model", "Monat", "Temperatur", "Batterietemperatur", "Geraet aktiv"]
#discard all columns to the right of “​​Geraet aktiv”


######### 

#Transform data
# Transform temperatures in Celsius to Fahrenheit (formula is (TemperatureInCelsius * 9/5) + 32) in place (keep the same column names)
# Columns Temperatur and Batterietemperatur

df["Temperatur"] = (df["Temperatur"].astype(str).str.replace(',', '.').astype(float)*9/5)+32
df["Batterietemperatur"] = (df["Batterietemperatur"].astype(str).str.replace(',', '.').astype(float)*9/5)+32

df["Temperatur"] = df["Batterietemperatur"] *(9/5)+32
df["Batterietemperatur"] = df["Batterietemperatur"]  *(9/5)+32


df["Monat"] = df["Monat"].astype(int).between(1, 12 , inclusive='both')
df["Geraet"] = df["Geraet"].astype(int)
data = df[(df['Geraet'] > 0)]   
    
df["Temperatur"] = df["Temperatur"].between(-459.67, 212)
df["Batterietemperatur"] =(df["Batterietemperatur"].between(-459.67, 212)) 

df["Geraet aktiv"]= df["Geraet aktiv"].isin(["Ja", "Nein"])
    

df = df.astype(types)





print(df)
    

 

#
#Write data into a SQLite database called “temperatures.sqlite”, in the table “temperatures”

 
df.to_sql("temperatures", 'sqlite:///temperatures.sqlite',if_exists='replace', index=False)
    
    
 
 

    
    
 

    
    
