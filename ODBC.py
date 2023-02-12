import pyodbc

print(pyodbc.drivers())

#conx_string = "driver={ODBC Driver 18 for SQL Server}; server=DESKTOP-GASDFD9\LOCALDB#C1B92AB9; database=Northwind; trusted_connection=YES;"
conx_string  = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-GASDFD9\LOCALDB#E0F07210"
            "Database=Northwind;"
            "Trusted_Connection=yes;")
# query = "SELECT Name, CreditRating FROM Purchasing.Vendor WHERE CreditRating < 3"
#
conx = pyodbc.connect(conx_string)
#
# cursor = conx.cursor()
#
# cursor.execute(query)
#
# data = cursor.fetchall()
#
# print(data[:5])



