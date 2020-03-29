import requests
import time
from time import sleep
from bs4 import BeautifulSoup
import mysql.connector
import re
from datetime import datetime


def get_rate(soup,href):
    score = soup.find('div', 'ratingContainer')
    max_try = 5
    n_try = 1
    while(score == None):
        if(n_try == max_try):
            break
        print("評分抓取重新嘗試... ", n_try)
        page = requests.get(href).text
        soup = BeautifulSoup(page, 'html.parser')
        score = soup.find('div', 'ratingContainer')
        n_try += 1
    if(score == None):
        return score
    else:
        rate = score.span['alt']
        Rate = re.findall(r'[\d\.\d]+', rate)
        new_rate = Rate[0]
        return new_rate


def get_comment(soup,href):
    comment = soup.find('span', 'reviewCount')
    max_try = 5
    n_try = 1
    while(comment == None):
        if(n_try == max_try):
            break
        print("評論數抓取重新嘗試... ", n_try)
        page = requests.get(href).text
        soup = BeautifulSoup(page, 'html.parser')
        comment = soup.find('span', 'reviewCount')
        n_try += 1
    if(comment == None):
        return comment
    else:
        c_comment = comment.get_text()
        Com = re.findall(r'[\d\,\d]+', c_comment)
        new_comment = int(Com[0].replace(",", ""))
        return new_comment

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test2'
)
taget_region = '台北'
sql = "SELECT id,comment,rate,href FROM `site_data` WHERE `city_name` = '" + "台東" + "'"
cursor = cnx.cursor()
cursor.execute(sql)

for each in cursor:
    s_id = each[0]
    past_comment = each[1]
    past_rate = each[2]
    href = each[3]

    print("正在更新", s_id, ".........")
    page = requests.get(href).text
    soup = BeautifulSoup(page, 'html.parser')
    score = soup.find('div', 'ratingContainer')
    new_rate = get_rate(soup,href)
    new_comment = get_comment(soup,href)
    if new_rate == None:
        new_rate = past_rate
    else:
        new_rate = float(new_rate)

    if new_comment == None:
        new_comment = past_comment
    else:
        new_comment = int(new_comment)
    
    if((past_rate != new_rate) or (past_comment != new_comment)):
        print(s_id,"更新資料")
        print("評分：",past_rate, "---------------->", new_rate)
        print("評論數：",past_comment, "---------------->", new_comment)
    else:
        print(s_id,"Nothing change!!")
    
    today = str(datetime.today().strftime('%Y/%m/%d'))
    print(s_id,"更新結束!!   更新日期：",today)
    print()

 