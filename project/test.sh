#!/bin/bash

if [[ "$(python -V)" =~ "Python 3" ]]
then
   echo Python is installed.
   python -c "import pandas"
   if [ $? -eq "0" ]
   then
     echo "pandas is installed"
   else
     pip install pandas 
   fi
      
   python -c "import sqlalchemy"
   if [ $? -eq "0" ]
   then
     echo "sqlalchemy is installed"
   else
     pip install sqlalchemy
     pip install sqlalchemy-databricks
   fi

   python -c "import openpyxl"
   if [ $? -eq "0" ]
   then
     echo "openpyxl is installed"
   else
     pip install openpyxl
   fi

cd data
python init.py
cd ..
cd ..
python -m unittest discover
else
   echo "please install python"
fi