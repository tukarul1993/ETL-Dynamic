import os
import mimetypes
import pandas as pd
import pyodbc
from Model import SQLConnection
from Model import DataTypeSelector
from Control import CreateTables
from Control import InsertData
import codecs
from io import StringIO

folderPath='D:\Python\ETL_ImportMultipleDataFiles\Files'

""" Function to load data into MSSQL from Dataframe """
def load_Data(df, file_path,file):
    CreateTables.CreateTables.create_table(df, file_path,file)
    InsertData.InsertData.insert_data(df, file_path,file)
def get_encoding(file):
    with open(file, 'rb') as f:
        contents = f.read()
        try:
            contents.decode('utf-8')
            return 'utf-8'
        except:
            pass
        try:
            contents.decode('utf-16')
            return 'utf-16'
        except:
            pass
        try:
            contents.decode('utf-32')
            return 'utf-32'
        except:
            pass
        return 'unknown'
def read_file(file, encoding):
    with codecs.open(file, 'r', encoding=encoding) as f:
        contents = f.read()
    return contents


def contents_to_dataframe(contents, separator=','):
    return pd.read_csv(StringIO(contents), sep=separator)


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
            encoding = get_encoding(file_path)
            contents = read_file(file_path, encoding)   ## Reads any encoding
            df = contents_to_dataframe(contents)
            #df = pd.read_csv(file_path)         ## reads only UTF-8 excoded files
        elif (file_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"):
            df = pd.read_excel(file_path)
        else:
            print("Unknow file format")

        load_Data(df, file_path,file)