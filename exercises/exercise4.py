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

 
def getDataFromFile(file_):
    df = pd.read_csv(file_, delimiter=';', index_col=False, usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])
    return df
    

def createSQLiteFile(df):
    df.to_sql("temperatures", 'sqlite:///temperatures.sqlite',if_exists='replace', index=False)
    
    
def changeDataType(df,types):
    df = df.astype(types)
    return df
    
    
    
def validateAndTransformData(data):
    
    data["Temperatur"] = (data["Temperatur"].astype(str).str.replace(',', '.').astype(float)*9/5)+32
  
    return data
    
def init():
    link = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
    file_ = getZipFileFromLink(link)

   

    
    
if __name__ == "__main__":
    init()  