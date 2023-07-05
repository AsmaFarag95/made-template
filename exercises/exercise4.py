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


def getZipFileFromLink(link):
    csv_file = "data.csv"
    urllib.request.urlretrieve(link, "md.zip")
    with zipfile.ZipFile("md.zip", 'r') as rref:
        rref.extract(csv_file)
    return csv_file
 
def getDataFromFile(file_):
    df = pd.read_csv(file_, delimiter=';', index_col=False, usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])
    df.columns =["Geraet", "Hersteller", "Model", "Monat", "Temperatur", "Batterietemperatur", "Geraet aktiv"]
    return df
    

def createSQLiteFile(df):
    df.to_sql("temperatures", 'sqlite:///temperatures.sqlite',if_exists='replace', index=False)
    
    
def changeDataType(df,types):
    df = df.astype(types)
    return df
    
    
    
def validateAndTransformData(data):
    
    data["Temperatur"] = (data["Temperatur"].astype(str).str.replace(',', '.').astype(float)*9/5)+32
    data["Batterietemperatur"] = (data["Batterietemperatur"].astype(str).str.replace(',', '.').astype(float)*9/5)+32
    data["Monat"] = data["Monat"].astype(int)
    data["Geraet"] = data["Geraet"].astype(int)
    data = data[(data['Geraet'] > 0) & (data['Monat'].between(1, 12))& (data["Temperatur"].between(-459.67, 212))& (data["Batterietemperatur"].between(-459.67, 212)) & (data["Geraet aktiv"].isin(["Ja", "Nein"]))]
    return data
    
def init():
    link = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
    file_ = getZipFileFromLink(link)
    df = getDataFromFile(file_)
    df = validateAndTransformData(df)
    df = changeDataType(df,types)
    print(df)
    createSQLiteFile(df)
   

    
    
if __name__ == "__main__":
    init()  