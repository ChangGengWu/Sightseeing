import mysql.connector
import re
print("=============start=============", end='\n')

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test1'
)
cursor = cnx.cursor(buffered=True)
query1 = "SELECT id,name FROM site"
cursor.execute(query1)
for each in cursor:
    id = each[0]
    name = each[1].split(" ")
    print(id + " " + name[0])
    cursor2 = cnx.cursor(buffered=True)
    query2 = ("UPDATE site"
              " SET name=%s"
              " WHERE id=%s")
    data = (name[0], id)
    cursor2.execute(query2, data)
    cnx.commit()
