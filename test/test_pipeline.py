import sys
import unittest
import pathlib as pl
import pandas as pd
import os

def pipeline():
        print("Fetching wroclaw transport data....")
        #download data from here: https://drive.google.com/file/d/1Dvi5y254IvaPujrixbIwZehmeHh2Ncu0/view?usp=sharing
        # wroclawDataFrame = pd.read_csv(r"C:\\Users\\mujeeb\\Downloads\\archive (1)\\positions.csv",usecols=[0, 3,4,5]) 
        # wroclawDataFrame= wroclawDataFrame[~(wroclawDataFrame["x"] > 90)]
        # wroclawDataFrame= wroclawDataFrame[~(wroclawDataFrame["y"] > 180)]

        # print("Fetching wroclaw transport data [done]....")
        # print("Fetching nuremberg transport data....")
        nurembergDataFrame = pd.read_excel('https://opendata.vag.de/dataset/08eb49f9-0f6c-4b76-96fd-5f8e3a0ac593/resource/c66d5b67-6a01-4190-a9cf-1de6359d07ae/download/20170601_haltestellen_id_geo.xlsx',
        usecols='C,H,G,F')
        print("Fetching nuremberg transport data [done]....")



        #==========Makeing Data and columns consistent for both datasets==========#
        print("Cleaning data and removing missing values....")




        # wroclawDataFrame.columns=["Haltepunkt","Betriebszweig","latitude","longitude"] 

        # wroclawDataFrame['Status'] = 'Unique'
        # wroclawDataFrame.loc[wroclawDataFrame[wroclawDataFrame.loc[:, ['latitude', 'longitude']].round(3).duplicated(keep=False)].index, 'Status'] = 'PD'
        # wroclawDataFrame.drop(index=wroclawDataFrame[wroclawDataFrame['Status'] == 'PD'].index, inplace=True)

        # wroclawDataFrame = wroclawDataFrame.replace(['tram'], 'T')
        # wroclawDataFrame = wroclawDataFrame.replace(['bus'], 'B')
        # wroclawDataFrame.dropna() #removing missing values if data has any missing values
        nurembergDataFrame.dropna() #removing missing values if data has any missing values
        print("Cleaning data and removing missing values [done]....")
        # print(wroclawDataFrame)
        # #================Creating db files=======================================
        print("Creating SQLite files....")
        print("creating wroclaw data table, it will take few minutes ...")
        # wroclawDataFrame.to_sql("wroclaw_data", 'sqlite:///wroclaw_nuremberg_public_transport.sqlite',if_exists='replace', index=False)
        print("creating wroclaw data table [done]...")
        print("creating nuremberg data table...")
        nurembergDataFrame.to_sql("nuremberg_data", 'sqlite:///wroclaw_nuremberg_public_transport.sqlite',if_exists='replace', index=False)
        print("creating nuremberg data table [done]...")
        print("SQLite files created successfully!")



        # # In[ ]:

pipeline()
class TestCase(unittest.TestCase):
    def test_SQLiteFileExists(self):
        directory_path = os.getcwd()
        assert os.path.exists(os.path.dirname(directory_path)+"\project\data\wroclaw_nuremberg_public_transport.sqlite")
         

if __name__ == "__main__":
    if len(sys.argv) > 1:
        TestCase.URL = sys.argv.pop()
        
    unittest.main()