#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine
#====Selecting only relevent cols===========#
# Haltepunkt
# latitude
# longitude
# Betriebszweig 


#==========Fetching data==========#
print("Fetching wroclaw transport data....")
wroclawDataFrame = pd.read_csv(r"C:\Users\mujeeb\Downloads\archive (1)\positions.csv",usecols=[0, 3,4,5]) #download data from here: https://drive.google.com/file/d/1Dvi5y254IvaPujrixbIwZehmeHh2Ncu0/view?usp=sharing
print("Fetching wroclaw transport data [done]....")
print("Fetching nuremberg transport data....")
nurembergDataFrame = pd.read_excel('https://opendata.vag.de/dataset/08eb49f9-0f6c-4b76-96fd-5f8e3a0ac593/resource/c66d5b67-6a01-4190-a9cf-1de6359d07ae/download/20170601_haltestellen_id_geo.xlsx',
 usecols='C,F,G,H')
print("Fetching nuremberg transport data [done]....")



#==========Makeing Data and columns consistent for both datasets==========#
print("Cleaning data and removing missing values....")
wroclawDataFrame.columns=["Haltepunkt","Betriebszweig","latitude","latitude"] 
wroclawDataFrame = wroclawDataFrame.replace(['tram'], 'T')
wroclawDataFrame = wroclawDataFrame.replace(['bus'], 'B')
wroclawDataFrame.dropna() #removing missing values if data has any missing values
nurembergDataFrame.dropna() #removing missing values if data has any missing values
print("Cleaning data and removing missing values [done]....")

#================Creating db files=======================================
print("Creating SQLite files....")
createDb = create_engine("sqlite:///wroclaw_nuremberg_public_transport.db")
print("DB created...")
print("creating wroclaw data table ...")
wroclawDataFrame.to_sql("wroclaw_data", createDb, if_exists="replace")
print("creating wroclaw data table [done]...")
print("creating nuremberg data table...")
nurembergDataFrame.to_sql("nuremberg_data", createDb, if_exists="replace")
print("creating nuremberg data table [done]...")
print("SQLite files created successfully!")


# In[ ]:




