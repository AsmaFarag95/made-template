#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
from sqlalchemy import create_engine

#====Selecting only relevent cols===========#
# Haltepunkt
# latitude
# longitude
# Betriebszweig 
#==========Fetching data==========#



def one_min_filter(timestamps,raw_df):
    itr = raw_df.iterrows()
    i, prev = next(itr)
    yield i
    for j, curr in itr:
        t1 = pd.to_datetime(prev['ts'])
        t2 = pd.to_datetime(curr['ts'])
        time_diff = pd.Timedelta(t2 - t1).seconds
        if (time_diff >= 500):
            yield j
            prev = curr


def pipeline():
        print("Fetching wroclaw transport data....")
        #download data from here: https://drive.google.com/file/d/1Dvi5y254IvaPujrixbIwZehmeHh2Ncu0/view?usp=sharing
        wroclawDataFrame = pd.read_csv(r"C:\\Users\\mujeeb\\Downloads\\archive (1)\\positions.csv",usecols=[0,2, 3,4,5,6]) 
        wroclawDataFrame= wroclawDataFrame[~(wroclawDataFrame["x"] > 90)]
        wroclawDataFrame= wroclawDataFrame[~(wroclawDataFrame["y"] > 180)]

        print("Fetching wroclaw transport data [done]....")
        print("Fetching nuremberg transport data....")
        nurembergDataFrame = pd.read_excel('https://opendata.vag.de/dataset/08eb49f9-0f6c-4b76-96fd-5f8e3a0ac593/resource/c66d5b67-6a01-4190-a9cf-1de6359d07ae/download/20170601_haltestellen_id_geo.xlsx',
        usecols='B,H,G,F')
        print("Fetching nuremberg transport data [done]....")



        #==========Makeing Data and columns consistent for both datasets==========#
        print("Cleaning data and removing missing values....")




        wroclawDataFrame.columns=["Haltepunkt","name","Betriebszweig","latitude","longitude","ts"] 
        
        wroclawDataFrame['Status'] = 'Unique'
        wroclawDataFrame.loc[wroclawDataFrame[wroclawDataFrame.loc[:, ['latitude', 'longitude']].round(4).duplicated(keep=False)].index, 'Status'] = 'PD'
        wroclawDataFrame.drop(index=wroclawDataFrame[wroclawDataFrame['Status'] == 'PD'].index, inplace=True)
        wroclawDataFrame = wroclawDataFrame.loc[list(one_min_filter(wroclawDataFrame.ts,wroclawDataFrame))]
        wroclawDataFrame = wroclawDataFrame.drop(wroclawDataFrame[wroclawDataFrame['Betriebszweig'].str.contains('bus')].sample(670).index)
        wroclawDataFrame = wroclawDataFrame.replace(['tram'], 'T')
        wroclawDataFrame = wroclawDataFrame.replace(['bus'], 'B')
        wroclawDataFrame.dropna() #removing missing values if data has any missing values
        nurembergDataFrame.dropna() #removing missing values if data has any missing values
        print("Cleaning data and removing missing values [done]....")
        print(wroclawDataFrame)
        # #================Creating db files=======================================
        print("Creating SQLite files....")
        print("creating wroclaw data table, it will take few minutes ...")
        wroclawDataFrame.to_sql("wroclaw_data", 'sqlite:///wroclaw_nuremberg_public_transport.sqlite',if_exists='replace', index=False)
        print("creating wroclaw data table [done]...")
        print("creating nuremberg data table...")
        nurembergDataFrame.to_sql("nuremberg_data", 'sqlite:///wroclaw_nuremberg_public_transport.sqlite',if_exists='replace', index=False)
        print("creating nuremberg data table [done]...")
        print("SQLite files created successfully!")



        # # In[ ]:




