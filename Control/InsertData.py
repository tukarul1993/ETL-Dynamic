import os
import mimetypes
import pandas as pd
import pyodbc
from Model import SQLConnection
from Model import DataTypeSelector
from Control import CreateTables



class InsertData:
    def insert_data(df, file_path,file):
        try:
            connection = SQLConnection.Connection.get_connection()
            # Insert data in tables
            columns = df.axes[1]
            #print(len(df.columns))
            # print(df.axes[1])
            file_Name = file.replace(".", "_")
            query = "Insert into " + file_Name + "("
            for column in columns:
                # print(column)
                query = query + " " + column + ","

            query = query[:-1] + "\n\t)"
            # print(query)
            PlaceHolders = ""
            for name, dtype in df.dtypes.items():
                PlaceHolders = PlaceHolders + "?,"
            for row in df.itertuples():
                cursor = connection.cursor()
                # print(row[1:])
                cursor.execute("INSERT INTO " + file_Name + "  VALUES (" + PlaceHolders[:-1] + ")", row[1:])
                #print("################")
                #print("INSERT INTO " + file_Name + "  VALUES (" + PlaceHolders[:-1] + ")", row[1:])
                print("data inserted")
            connection.commit()
            connection.close()
        except:
            print('Error while creating table for file '+file_path)

