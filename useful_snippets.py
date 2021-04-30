# Read Binary Excel File
import pandas as pd
import pyxlsb
df =  pd.read_excel('Customers.xlsb', engine='pyxlsb', sheet_name = 'Sheet1')
df.shape



# Read data from MySQL database
import mysql.connector
import pandas as pd
connection  = mysql.connector.connect(user='public',  password='text@321', host='localhost', database='test_db')
query = "SELECT * FROM dbn.table"
df = pd.read_sql_query(query, connection)
