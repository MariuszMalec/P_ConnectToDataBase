#pip install mysql-connector-python

# trzeba zainstalowowac xampp!! i odpalic
# odpalic MySql Workbench

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='MySqlCityDb',
                                         user='root',
                                         password='',
                                         auth_plugin='mysql_native_password')

    mySql_Select_Query = """select * from City; """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Select_Query)
    record = cursor.fetchall()
    print("Your connected to database: ", record)

except mysql.connector.Error as error:
    print("Failed to select table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
