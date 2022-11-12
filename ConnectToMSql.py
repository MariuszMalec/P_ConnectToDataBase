#pip install pyodbc

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\\SQLEXPRESS;'
                      'Database=MainAppTrainersEventsDb;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM trainers')

for i in cursor:
    print(i)