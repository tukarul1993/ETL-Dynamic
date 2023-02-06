import pyodbc

class Connection:

    def get_connection():
        try:
            connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=ITLNB619;'
                    'DATABASE=SSIS_Practice;'
                    'UID=sa;'
                    'PWD=admin@123'
                )

            return connection
        except:
            print("Error while establishing connection")