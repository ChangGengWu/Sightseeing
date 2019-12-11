import sys
import jieba
import jieba.analyse
import mysql.connector
import re

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test1'
)
cursor = cnx.cursor(buffered=True)


query = "SELECT COMMENT FROM `user_comment` WHERE site_ID = 'S0099'"
cursor.execute(query)
for cmt in cursor:
    print
