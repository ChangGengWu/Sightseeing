from selenium import webdriver
import requests
import time
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import re

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test2',
    buffered=True
)
cursor = cnx.cursor()
cursor2 = cnx.cursor()
sql = "SELECT id FROM `hotel_data`"
cursor.execute(sql)
for id in cursor:
    num = re.findall(r'[\d\.\d]+', id[0])
    num = int(num[0])
    last_id = 'H{0:05}'.format(num)
    query2 = ("UPDATE hotel_data"
              " SET id=%s"
              " WHERE id=%s")
    data = (last_id, id[0])
    cursor2.execute(query2, data)
    cnx.commit()
