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

#取得所有景點資訊


def getSites(city_name,url):
    #連到目標網址
    driver.get(url)
    driver.implicitly_wait(5)
    #先點擊看更多
    seemore = "//span[contains(@class, 'ui_icon single-chevron-down single-chevron-down')]"
    driver.find_element_by_xpath(seemore).click()

    #宣告第一頁與其他頁抓取每個景點url的path
    p1_each = "//a[contains(@class, 'attractions-attraction-overview-pois-PoiInfo__name--SJ0a4')]"
    rest_each = "//div[contains(@class, 'tracking_attraction_title listing_title')]/a"

    #確認最後一頁連結作為終止點
    # lastPage = driver.find_elements_by_xpath(
    #     "//div[contains(@class, 'attractions-attraction-overview-main-Pagination__link--2m5mV attractions-attraction-overview-main-Pagination__cx_brand_refresh_phase2--3XKui')]/a").get_attribute('href')
    lastPage = "https://www.tripadvisor.com.tw/Attractions-g293912-Activities-oa300-Tainan.html"

    #當搜尋到最後一頁stop
    page = 1
    while(driver.current_url != lastPage):
        #第一頁與其他頁程式內容不同
        if(page == 1):
            #每個景點的url
            all_Sites = driver.find_elements_by_xpath(p1_each)
            #將該頁的所有url傳給to_each_site()
            each_Info(city_name, all_Sites)
        else:
            all_Sites = driver.find_elements_by_xpath(rest_each)
            each_Info(city_name, all_Sites)
        #點擊下一頁
        try:
            driver.implicitly_wait(5)
            next = driver.find_element_by_link_text('下一步')
            webdriver.ActionChains(driver).move_to_element(
                next).click(next).perform()
            page += 1
        except NoSuchElementException:
            break


def each_Info(city_name,all_url):
    for each in all_url:
        url = each.get_attribute('href')
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        #景點名稱
        name = ""
        try:
            name = soup.find('h1', id='HEADING').get_text().strip()
            name_temp = name.split(" ")
            name = name_temp[0]
        except AttributeError:
            try:
                page = requests.get(url).text
                soup = BeautifulSoup(page, 'html.parser')
                name = soup.find('h1', id='HEADING').get_text().strip()
                name_temp = name.split(" ")
                name = name_temp[0]
            except AttributeError:
                pass
        #景點地址
        try:
            address = soup.find(
                'span', 'textAlignWrapper address').get_text().strip()
        except AttributeError:
            address = "None"
        #景點評等
        try:
            score = soup.find('div', 'ratingContainer')
            rate = score.span['alt']
            Rate = re.findall(r'[\d\.\d]+', rate)
            rate = Rate[0]
        except AttributeError:
            rate = "None"
        #評論數
        try:
            comment = soup.find(
                'span', 'attractions-attraction-review-header-attraction-review-header__reviewCount--3cEMP attractions-attraction-review-header-attraction-review-header__dotted_link--3p26D')
            c_comment = comment.get_text()
            Com = re.findall(r'[\d\,\d]+', c_comment)
            c_comment = int(Com[0].replace(",", ""))
        except AttributeError:
            c_comment = "None"
        #類別
        lst_tag = []
        try:
            tags = soup.find('div', 'detail').findAll('a')
            for i in tags:
                if(i.get_text() == "更多"):
                    pass
                else:
                    lst_tag.append(i.get_text().strip())
        except AttributeError:
            pass
        ct_name = city_name

        new_id = get_newID()
        data_type = "site"
        #id,name,city,address,type,comment,rate,href
        add_Data(new_id, name, ct_name, address,
                 data_type, c_comment, rate, url)
        add_Relationship(new_id, lst_tag)

        print("景點名：" + name + " 分數：" + rate + " 評論數：",
              str(c_comment) + " 位置：" + address + " href：" + url + "TAG", lst_tag)
    print("="*100)

def get_newID():
    last_id = ""
    query = "SELECT MAX(id) FROM site_data"
    cursor.execute(query)
    for id in cursor:
        num = re.findall(r'[\d\.\d]+', id[0])
        num = int(num[0]) + 1
        last_id = 'S{0:04}'.format(num)
    return last_id

#加入site資料到資料庫
def add_Data(id,name,city_name,address,type,c_cmt,rate,href):
    add_data = ("INSERT INTO site_data"
                "(id,name,city_name,address,type,comment,rate,href) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (id, name, city_name , address , type , c_cmt , rate , href)
    cursor.execute(add_data, data)
    cnx.commit()

#加入連結到資料庫
def add_Relationship(s_id,tags):
    add_data = ("INSERT INTO `site_relationship`"
                "(`from`, `to`) "
                "VALUES (%s,%s)")
    for i in range(len(tags)):
        query = "SELECT id FROM site_attr WHERE tag = '" + tags[i] +"'"
        cursor.execute(query)
        for each in cursor:
            data = (s_id, each[0])
            cursor.execute(add_data, data)
            cnx.commit()


#Main
tStart = time.time()
driver = webdriver.Chrome("chromedriver")
target = [
          ["台南", "https://www.tripadvisor.com.tw/Attractions-g293912-Activities-Tainan.html"]]

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test3'
)
cursor = cnx.cursor(buffered=True)
for i in range(len(target)):
    getSites(target[i][0], target[i][1])
tEnd = time.time()
print("Run Time：", tEnd - tStart)
