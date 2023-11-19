#!/usr/bin/env python
 
import pandas as pd
from sqlalchemy import create_engine

def pipeline():


    print("Loadin Renewable Energy of the city of Münster in the years 1990-2020 data....")
        #download data from here:https://opendata.stadt-muenster.de/sites/default/files/Muenster-Erneuerbare-Energien_2020.xls
    RenewableEnergyUrl = "https://opendata.stadt-muenster.de/sites/default/files/Muenster-Erneuerbare-Energien_2020.xls" # 
    RenewableEnergy = pd.read_excel(RenewableEnergyUrl)
  

    print("Loadin CO2 emissions of the city of Münster in the years 1990-2021 data....")
        #download data from here: https://opendata.stadt-muenster.de/sites/default/files/Muenster-CO2-Emissionen_2021.xls
    CO2emissionsUrl = "https://opendata.stadt-muenster.de/sites/default/files/Muenster-CO2-Emissionen_2021.xls" # 
    CO2emissions = pd.read_excel(CO2emissionsUrl, sheet_name=None) # to add all the sheets


    #Cleaning data and removing missing values
    print("Cleaning data and removing missing values....")
    #CO2emissions.dropna(inplace=True)
    RenewableEnergy.dropna(inplace=True)

    print("Cleaning data and removing missing values [done]....")
    
    #Creating SQLite files
    print("Creating SQLite files: ")
    
    print("creating CO2emissions data table ...")
    for sheet_name, df in CO2emissions.items():
        df.to_sql(f"CO2emissions_{sheet_name}", 'sqlite:///CO2emissions_and_RenewableEnergy.sqlite', if_exists='replace', index=False)

    #CO2emissions.to_sql("CO2emissions_data", 'sqlite:///CO2emissions_and_RenewableEnergy.sqlite',if_exists='replace', index=False)
    
    print("creating RenewableEnergy data table...")
    RenewableEnergy.to_sql("RenewableEnergy", 'sqlite:///CO2emissions_and_RenewableEnergy.sqlite',if_exists='replace', index=False)
    
    print("SQLite files created successfully!")

pipeline()

