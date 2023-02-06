import os
import mimetypes
import pandas as pd
import pyodbc
from Model import SQLConnection
from Model import DataTypeSelector
from Control import CreateTables
from Control import InsertData

folderPath='D:\Python\ETL_ImportMultipleDataFiles\Files'

""" Function to load data into MSSQL from Dataframe """
def load_Data(df, file_path,file):
    CreateTables.CreateTables.create_table(df, file_path,file)
    InsertData.InsertData.insert_data(df, file_path,file)

""" Main program starts here """
if (folderPath):
    files = [f for f in os.listdir(folderPath)
             if os.path.isfile(os.path.join(folderPath, f))]

    for file in files:
        #print(file)
        file_path = os.path.join(folderPath, file)
        file_type = mimetypes.guess_type(file_path)[0]
        print(file_path)
        print(file_type)

        if (file_type == "application/vnd.ms-excel" or file_type == "text/plain"):
            df = pd.read_csv(file_path)         ## reads only UTF-8 excoded files
        elif (file_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"):
            df = pd.read_excel(file_path)
        else:
            print("Unknow file format")

        load_Data(df, file_path,file)