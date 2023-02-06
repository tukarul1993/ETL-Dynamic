
""" Data type selector for table creation query as per based on Input column typpes
    as of now, all kept as varchar(500)
"""

class DataTypeSelector:
    def getDatatype(self,argument):
        # print(argument)
        switcher = {
            "int64": " varchar(500)",
            "object": " varchar(500)",
            "float64": " varchar(500)",
            "datetime64[ns]": " varchar(500)"
        }
        return switcher.get(argument, " varchar(500)")