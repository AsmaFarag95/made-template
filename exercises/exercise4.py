import pandas as pd
import zipfile
import urllib.request


data_types = {
        'Geraet': int,
        'Hersteller': str,
        'Model': str,
        'Monat': int,
        'Temperatur': float,
        'Batterietemperatur': float,
        'Geraet aktiv': str
        }


def get_zip_file_from_link(url):
    csv_file = "data.csv"
    urllib.request.urlretrieve(url, "mowesta_dataset.zip")
    with zipfile.ZipFile("mowesta_dataset.zip", 'r') as rref:
        rref.extract(csv_file)
    return csv_file
 
def get_data_from_file(file_cv):

# Only use the columns "Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"
# Rename "Temperatur in °C (DWD)" to "Temperatur"
# Rename "Batterietemperatur in °C" to "Batterietemperatur"

    df = pd.read_csv(file_cv, delimiter=';', index_col=False, usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])
    df.columns =["Geraet", "Hersteller", "Model", "Monat", "Temperatur", "Batterietemperatur", "Geraet aktiv"]
    
# Discard all columns to the right of "Geraet aktiv"
    df = df.loc[:, :"Geraet aktiv"]
    
    return df
    

    
def fitting_data_types(df,types):
    df = df.astype(types)
    return df
    
    


      
def validations_as(data):
    # Transform temperatures in Celsius to Fahrenheit

    data["Temperatur"] = (data["Temperatur"].astype(str).str.replace(',', '.').astype(float)*9/5)+32
    data["Batterietemperatur"] = (data["Batterietemperatur"].astype(str).str.replace(',', '.').astype(float)*9/5)+32
    data["Monat"] = data["Monat"].astype(int)
    data["Geraet"] = data["Geraet"].astype(int)
    data = data[(data['Geraet'] > 0) & (data['Monat'].between(1, 12, inclusive='both'))& (data["Temperatur"].between(-459.67, 212))& (data["Batterietemperatur"].between(-459.67, 212)) & (data["Geraet aktiv"].isin(["Ja", "Nein"]))]
    return data


def create_SQLite_file(df):
    df.to_sql("temperatures", 'sqlite:///temperatures.sqlite',if_exists='replace', index=False )
    
    
def init():
    url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
    file_cv = get_zip_file_from_link(url)
    df = get_data_from_file(file_cv)
    df = validations_as(df)
    df = fitting_data_types(df,data_types)
    print(df)
    create_SQLite_file(df)
   

    
    
if __name__ == "__main__":
    init()  