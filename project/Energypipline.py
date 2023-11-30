#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

def pipeline():

#loading the data:
    print("Loadin Renewable Energy of the city of Münster in the years 1990-2020 data....")
        #download data from here:https://opendata.stadt-muenster.de/sites/default/files/Muenster-Erneuerbare-Energien_2020.xls
    RenewableEnergyUrl = "https://opendata.stadt-muenster.de/sites/default/files/Muenster-Erneuerbare-Energien_2020.xls" # 
    RenewableEnergy = pd.read_excel(RenewableEnergyUrl)
  

    print("Loadin CO2 emissions of the city of Münster in the years 1990-2021 data....")
        #download data from here: https://opendata.stadt-muenster.de/sites/default/files/Muenster-CO2-Emissionen_2021.xls
    CO2emissionsUrl = "https://opendata.stadt-muenster.de/sites/default/files/Muenster-CO2-Emissionen_2021.xls" # 
    CO2emissions = pd.read_excel(CO2emissionsUrl, sheet_name=None) # to add all the three  sheets  into CO2emissions data frame,  because it loads the first one by default.


#store each sheet in a data frame >>>  then creat a new CO2emissions data frame from these data frames:
    CO2emissions_sectors  = pd.read_excel(CO2emissionsUrl, sheet_name=0) # the first sheet (at 0) define CO2emissions by sectors
    CO2emissions_sectors =CO2emissions_sectors.rename(columns={'CO2-Emissionen nach Sektoren in (t)': 'year'} ) #rename the CO2-Emissionen nach Sektoren column into >>> year 
    #CO2emissions_sectors.index.name = 'CO2 emissions according to sector in (t)' # put the dataset topic in the first(index) column

    CO2emissions_applications = pd.read_excel(CO2emissionsUrl, sheet_name=1)
    CO2emissions_applications =CO2emissions_applications.rename(columns={'CO2-Emissionen nach Anwendungen in (kt)': 'year'} ) #rename the CO2-Emissionen nach Anwendungen column into >>> year 
   # CO2emissions_applications.index.name = 'CO2 emissions according to applications in (KT)' # put the dataset topic in the first(index) column


    CO2emissions = pd.merge(CO2emissions_sectors, CO2emissions_applications,  on='year' ) #merge the two exel sheets into one datafram. 
    CO2emissions =CO2emissions.rename(columns={'Verkehr_x': 'Verkehr_Sektoren'}) # rename for readability
    CO2emissions =CO2emissions.rename(columns={'Verkehr_y': 'Verkehr_Anwendungen'}) # rename for readability
    CO2emissions =CO2emissions.rename(columns={'Gesamt_x': 'Gesamt_Sektoren'}) # rename for readability
    CO2emissions =CO2emissions.rename(columns={'Gesamt_y': 'Gesamt_Anwendungen'}) # rename for readability
    CO2emissions = CO2emissions.drop(['Verkehr in %', 'Wärme in %', 'Strom in %'], axis=1) #delete these columns
    CO2emissions = CO2emissions[['year', 'Private Haushalte', 'Gewerbe + Sonstiges', 'Industrie',  'Wärme', 'Strom',  'Verkehr_Sektoren' ,'Verkehr_Anwendungen' , 'Gesamt_Sektoren' , 'Gesamt_Anwendungen', 'Gesamt in % zu 1990']] # reannage columns
    
    


#Cleaning data and removing missing values

    print("Cleaning data and removing missing values....")
    RenewableEnergy.dropna(inplace=True)
    CO2emissions.dropna(inplace=True)

    print("Cleaning data and removing missing values [done]....")
    

#Creating SQLite files
    print("Creating SQLite files: ")

    print("creating CO2emissions data table ...")
    CO2emissions.to_sql("CO2emissions", 'sqlite://///Users/asmafaraj/Downloads/FAUWINTER/made/made-template/data/CO2emissionsRenewableEnergy.sqlite', if_exists='replace', index=False)
   
     
    print("creating RenewableEnergy data table...")
    RenewableEnergy.to_sql("RenewableEnergy", 'sqlite://///Users/asmafaraj/Downloads/FAUWINTER/made/made-template/data/CO2emissionsRenewableEnergy.sqlite' ,if_exists='replace', index=False)

#Creating SQLite files:
 
    print("Creating SQLite files: ")

    print("creating CO2emissions data table ...")
    CO2emissions.to_sql("CO2emissions", 'sqlite:////data/CO2emissionsRenewableEnergy.sqlite',if_exists='replace', index=False)
   
     
    print("creating RenewableEnergy data table...")
    RenewableEnergy.to_sql("RenewableEnergy", 'sqlite:////data/CO2emissionsRenewableEnergy.sqlite',if_exists='replace', index=False)

    
    print("SQLite files created successfully!")
    

pipeline()

