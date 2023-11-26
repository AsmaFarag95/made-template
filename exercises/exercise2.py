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

def createSQLiteFile(data_frame):
    data_frame.to_sql("trainstops", 'sqlite:///trainstops.sqlite',if_exists='replace', index=False)
    
    
def changeDataType(data_frame,types):
    data_frame = data_frame.astype(types)
    return data_frame
    
    
    
def cleanData(data_frame):
    data_frame.drop(columns=["Status"], inplace=True)
    data_frame = data_frame[data_frame["Verkehr"].isin(["FV","RV","nur DPN"])]

    data_frame['Laenge'] = data_frame['Laenge'].str.replace(',','.')
    data_frame['Breite'] = data_frame['Breite'].str.replace(',','.')


    data_frame = data_frame.dropna()
    data_frame = changeDataType(data_frame, types)

    data_frame = data_frame[~((data_frame["Laenge"] <= 90) & (data_frame["Laenge"] >= -90))]
    data_frame = data_frame[~((data_frame["Breite"] <= 90) & (data_frame["Breite"] >= -90))]

    data_frame = data_frame[data_frame['IFOPT'].str.contains(r'^[a-zA-Z]{2}:[0-9]*:[0-9]+(:[0-9]+)?$')]
    data_frame.IFOPT = data_frame.IFOPT.astype(str)
    return data_frame

    
def init():
    csv_link = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
 #call the methods:
    data_frame = getDataFromLink(csv_link)
    data_frame = cleanData(data_frame)
    createSQLiteFile(data_frame)

    
    
if __name__ == "__main__":
    init()  

  
