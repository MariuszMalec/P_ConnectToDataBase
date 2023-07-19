#Only Python
# zainstalowa pythons
# pip install mysql-connector-python
# przy bledzie autoryzacji mui byc to dodane  auth_plugin='mysql_native_password'
# database movieDb/Mario@13/Alicja@13/Movies
# in visual studio code: python3 ConnectToMySql.py
# jesli nie dziala to odinstalowac connector i zainstalowac ponownie!

# Only windows
# zaintstalowac MySql Workbench
# trzeba zainstalowowac dodoatkowoxampp!! i odpalic
# odpalic xxamp, wybrac apache i mysql

import mysql.connector
from mysql.connector import Error

try:
    
    connection = mysql.connector.connect(host='localhost',
                                         database='mainappTrackingDb',
                                         user='root',
                                         password='',
                                         auth_plugin='mysql_native_password')  
     
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
