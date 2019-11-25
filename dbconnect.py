import mysql.connector
import re

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test1'
)
print(cnx)
cursor = cnx.cursor()

# for i in range(1,10):
#     num = '{0:04}'.format(i)
#     id = "TD"+num
#     add_data = ("INSERT INTO site""(id,name) ""VALUES (%s, %s)")
#     data = (id,"3")
#     cursor.execute(add_data, data)

query = "SELECT id FROM attr WHERE attr = " + "'景點和地標'"
print(query)
cursor.execute(query)
for each in cursor:
    print(each[0])

# def to_StringID(stringID):
