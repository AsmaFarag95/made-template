import pandas as pd


def getDataFromLink(link):
    dataFrame = pd.read_csv(link, delimiter=";")
    return dataFrame
    


def createSQLiteFile(df):
    df.to_sql("trainstops", 'sqlite:///trainstops.sqlite',if_exists='replace', index=False)
    
    

    
def cleanData(data):
    data.drop(columns=["Status"], inplace=True)
    data = data[data["Verkehr"].isin(["FV","RV","nur DPN"])]
    data['Laenge'] = data['Laenge'].str.replace(',','.')
    data['Breite'] = data['Breite'].str.replace(',','.')
    data["Laenge"] = pd.to_numeric(data["Laenge"])
    data["Breite"] = pd.to_numeric(data["Breite"])
    data["EVA_NR"] = pd.to_numeric(data["EVA_NR"])
    data["Betreiber_Nr"] = pd.to_numeric(data["Betreiber_Nr"])
    data= data[~(data["Laenge"] < 90) & data["Laenge"] > -90]
    data= data[~(data["Breite"] < 90) & data["Breite"] > -90]
    data = data.dropna()
    data = data[data['IFOPT'].str.contains(r'^[a-zA-Z]{2}:[0-9]*:[0-9]+(:[0-9]+)?$')]
    return data
    

link = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
df = getDataFromLink(link)
df = cleanData(df)
createSQLiteFile(df)