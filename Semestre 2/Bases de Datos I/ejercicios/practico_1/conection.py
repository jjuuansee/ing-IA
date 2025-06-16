import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpassword",
)

cursor = connection.cursor()
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

connection.close()
