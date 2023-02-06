import os
import mimetypes
import pandas as pd
import pyodbc
from Model import SQLConnection
from Model import DataTypeSelector
from Control import CreateTables

class CreateTables:
    def create_table(df, file_path,file):
        try:
            """ Create tables for each file """
            ColNames = ""
            connection = SQLConnection.Connection.get_connection()
            # print(connection)
            file_Name = file.replace(".", "_")
            # print(file_Name )

            for name, dtype in df.dtypes.items():
                # print(dtype)
                ColNames = ColNames + name + ","
            # print(ColNames[:-1])

            SQL = " IF OBJECT_ID(N'" + file_Name + "') IS NOT NULL \n" \
                                                   " BEGIN\n" \
                                                   " DROP TABLE " + file_Name + "\n" \
                                                                                " END\n" \
                                                                                " create table " + file_Name + " (\n\t"
            dataTS = DataTypeSelector.DataTypeSelector()

            for name, dtype in df.dtypes.items():
                # print(name, dtype)
                SQL = SQL + "[" + str(name.strip()) + "]" + \
                      dataTS.getDatatype((str(dtype))) + ","
            SQL = SQL[:-1] + "\n\t)"

            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()
            connection.close()

            print("Tables created")

        except:
            print('Error while creating table for file '+file_path)

