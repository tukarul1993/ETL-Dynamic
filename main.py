import os
import pandas as pd
from Model import GetEncoding
#import pyodbc
import mimetypes
#import csv
#from SQLConnection import Connection
#from model import DataTypeSelector
from Model import ReadFile


path = 'D:\Python\ETL_ImportMultipleDataFiles\Files'
if (path):
    files = [f for f in os.listdir(path)
             if os.path.isfile(os.path.join(path, f))]
    for file in files:
        print(file)
        file_path = os.path.join(path, file)

        file_type = mimetypes.guess_type(file_path)[0]

        if (file_type == "application/vnd.ms-excel" or file_type == "text/plain"):
            df = pd.read_csv(file_path)
            # display the first 5 rows of the dataframe
            # print(df.head())
        elif (file_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"):
            df = pd.read_excel(file_path)
            # print(df.head())
        elif (file_type == "application/json"):
            df = pd.read_json("D:\Python\ETL_with_python\Files\JsonDataFile.json")
            print(df)
        else:
            print("Unknow file format")





        ge = GetEncoding.GetEncoding()
        encoding = ge.get_encoding(file_path)

        contents=ReadFile.ReadFile.read_file(file_path, encoding)
        #print(contents)

