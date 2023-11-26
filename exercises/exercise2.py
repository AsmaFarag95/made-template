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
    data_frame.loc[:, 'Laenge'] = data_frame['Laenge'].str.replace(',', '.')
    data_frame.loc[:, 'Breite'] = data_frame['Breite'].str.replace(',', '.')


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
