import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',         # or your server IP / hostname
        database='your_database', # name of the MySQL database
        user='your_username',     # your MySQL username
        password='your_password'  # your MySQL password
    )

    if connection.is_connected():
        print("Successfully connected to the database")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
