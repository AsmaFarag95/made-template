#!/bin/bash
python3 project/Energypipline.py

   echo Python is installed.
   python3 -c "import pandas"
   if [ $? -eq "0" ]
   then
     echo "pandas is installed"
   else
     pip3 install pandas 
   fi
      
   python3 -c "import sqlalchemy"
   if [ $? -eq "0" ]
   then
     echo "sqlalchemy is installed"
   else
     pip3 install sqlalchemy
     pip3 install sqlalchemy-databricks
   fi

   python3 -c "import openpyxl"
   if [ $? -eq "0" ]
   then
     echo "openpyxl is installed"
   else
     pip3 install openpyxl
   fi

# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "dirname: $SCRIPT_DIR"
echo "pwd: $pwd"
# Construct the relative path to the SQLite database
DB_RELATIVE_PATH="made-template/data/CO2emissionsRenewableEnergy.sqlite"

# Construct the full path to the SQLite database
DB_PATH="$SCRIPT_DIR/$DB_RELATIVE_PATH"

# Check if the SQLite database is created
if [ -f "$DB_PATH" ]; then
  echo "SQLite database created successfully."
else 
  echo "SQLite database not created."
  exit 1
fi


# Check if specific tables exist in SQLite databases,  #check the path carfully
if sqlite3  /made-template/data/CO2emissionsRenewableEnergy.sqlite  "SELECT name FROM sqlite_master WHERE type='table' AND name='CO2emissions';" | grep CO2emissions &&
   sqlite3  /made-template/data/CO2emissionsRenewableEnergy.sqlite  "SELECT name FROM sqlite_master WHERE type='table' AND name='RenewableEnergy';" | grep RenewableEnergy; then
  echo "Tables exist in SQLite databases."
else
  echo "Tables not found in SQLite databases."
  exit 1
fi



# Return an appropriate exit status
# 0 means success, non-zero means failure
exit 0


# python -m unittest discover
