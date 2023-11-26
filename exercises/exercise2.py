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
    data_frame = pd.read_csv(link, delimiter=";")
    return data_frame

def createSQLiteFile(df):
    df.to_sql("trainstops", 'sqlite:///trainstops.sqlite',if_exists='replace', index=False)
    
    
def changeDataType(df,types):
    df = data_frame.astype(types)
    return df
    
    
    
def cleanData(df):
    df.drop(columns=["Status"], inplace=True)
    df = data_frame[df["Verkehr"].isin(["FV","RV","nur DPN"])]

    df['Laenge'] = df['Laenge'].str.replace(',','.')
    df['Breite'] = df['Breite'].str.replace(',','.')


    df = df.dropna()
    df = changeDataType(df, types)

    df = df[~((df["Laenge"] <= 90) & (df["Laenge"] >= -90))]
    df = df[~((df["Breite"] <= 90) & (df["Breite"] >= -90))]

    df = df[df['IFOPT'].str.contains(r'^[a-zA-Z]{2}:[0-9]*:[0-9]+(:[0-9]+)?$')]
    df.IFOPT = df.IFOPT.astype(str)
    return df

    
def init():
    csv_link = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
 #call the methods:
    data_frame = getDataFromLink(csv_link)
    data_frame = cleanData(data_frame)
    createSQLiteFile(data_frame)

    
    
if __name__ == "__main__":
    init()  

  
