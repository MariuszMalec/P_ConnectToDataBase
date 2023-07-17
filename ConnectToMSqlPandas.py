import pandas as pd
import pyodbc

import warnings

warnings.filterwarnings('ignore')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\\SQLEXPRESS;'
                      'Database=mainappTrackingDb;'
                      'Trusted_Connection=yes;')

df = pd.read_sql_query('SELECT * FROM trainers', conn)

print(df)
print(type(df))