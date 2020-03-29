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


def getSites(city_name, url):
    #連到目標網址
    sleep(5)
    driver.get(url)
    sleep(5)
    driver.implicitly_wait(5)
    #宣告第一頁與其他頁抓取每個景點url的path
    p1_each = "//a[contains(@class, 'property_title prominent')]"

    #確認最後一頁連結作為終止點
    lastPage = driver.find_element_by_xpath(
        "//a[contains(@class, 'pageNum last ')]").get_attribute('href')

    #當搜尋到最後一頁stop
    page = 1
    while(driver.current_url != lastPage):
        all_Sites = driver.find_elements_by_xpath(p1_each)
        each_Info(city_name, all_Sites)
        #點擊下一頁
        try:
            driver.implicitly_wait(5)
            nextPage_url = driver.find_element_by_xpath(
            "//a[contains(@class, 'nav next ui_button primary')]").get_attribute('href')
            driver.get(nextPage_url)
            sleep(15)
            driver.implicitly_wait(5)
            page += 1
        except NoSuchElementException:
            break


def each_Info(city_name, all_url):
    for each in all_url:
        url = each.get_attribute('href')
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        #景點名稱
        name = ""
        try:
            name = soup.find('h1', id='HEADING').get_text().strip()
            name_temp = name.split(" ")
            #取中文部分
            name = name_temp[0]
        except AttributeError:
            try:
                page = requests.get(url).text
                soup = BeautifulSoup(page, 'html.parser')
                name = soup.find('h1', id='HEADING').get_text().strip()
                #取中文部分
                name_temp = name.split(" ")
                name = name_temp[0]
            except AttributeError:
                pass
        #景點地址
        try:
            address = soup.find(
                'span', 'public-business-listing-ContactInfo__ui_link--1_7Zp public-business-listing-ContactInfo__level_4--3JgmI').get_text().strip()
        except AttributeError:
            address = "None"
        #景點評等
        try:
            rate = soup.find(
                'span', 'hotels-hotel-review-about-with-photos-Reviews__overallRating--vElGA').text
        except AttributeError:
            rate = "None"
        #評論數
        try:
            comment = soup.find(
                'span', 'hotels-hotel-review-about-with-photos-Reviews__seeAllReviews--3PpLR')
            c_comment = comment.get_text()
            Com = re.findall(r'[\d\,\d]+', c_comment)
            c_comment = int(Com[0].replace(",", ""))
        except AttributeError:
            c_comment = "None"
        #類別
        tag_lst = []
        try:
            facility = soup.find_all('div', {'data-test-target': 'amenity_text'})
            for i in facility:
                tag_lst.append(i.get_text())
        except AttributeError:
            pass
        ct_name = city_name
        new_id = get_newID()
        #id,name,city,address,type,comment,rate,href
        add_Data(new_id, name, ct_name, address,c_comment, rate, url)
        add_Relationship(new_id, tag_lst)
        print("飯店名：" + name + " 分數：" + rate + " 評論數：",
              str(c_comment) + " 位置：" + address + " href：" + url )
    print("="*100)


def get_newID():
    last_id = ""
    query = "SELECT MAX(id) FROM hotel_data"
    cursor.execute(query)
    for id in cursor:
        num = re.findall(r'[\d\.\d]+', id[0])
        num = int(num[0]) + 1
        last_id = 'H{0:05}'.format(num)
    return last_id

#加入site資料到資料庫
def add_Data(id, name, city_name, address, c_cmt, rate, href):
    add_data = ("INSERT INTO hotel_data"
                "(id,name,city_name,address,comment,rate,href) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    data = (id, name, city_name, address, c_cmt, rate, href)
    cursor.execute(add_data, data)
    cnx.commit()

#加入連結到資料庫
def add_Relationship(s_id, tags):
    check_exist(tags)
    add_data = ("INSERT INTO `hotel_relationship`"
                "(`from_id`, `to_id`) "
                "VALUES (%s,%s)")
    for i in tags:
        query = "SELECT id FROM hotel_attr WHERE tag = '" + i + "'"
        cursor.execute(query)
        for each in cursor:
            data = (s_id, each[0])
            cursor.execute(add_data, data)
            cnx.commit()

def check_exist(tags):
    for each in tags:
        sql = "SELECT id FROM hotel_attr WHERE tag = '" + each + "'"
        cursor.execute(sql)
        entry = cursor.fetchone()
        if entry is None:
            print(each,"++++++++")
            add_data = ("INSERT INTO hotel_attr"
                        "(id, tag) "
                        "VALUES (%s,%s)")
            data = ("", each)
            cursor.execute(add_data, data)
            cnx.commit()


#Main
tStart = time.time()
driver = webdriver.Chrome("chromedriver")

target = [
    ["南投", "https://www.tripadvisor.com.tw/Hotels-g304160-Nantou-Hotels.html"]]


# [["台北", "https://www.tripadvisor.com.tw/Hotels-g293913-Taipei-Hotels.html"]]
# [["新北", "https://www.tripadvisor.com.tw/Hotels-g1432365-New_Taipei-Hotels.html"]]
# [["桃園", "https://www.tripadvisor.com.tw/Hotels-g297912-Taoyuan-Hotels.html"]]
# [["基隆", "https://www.tripadvisor.com.tw/Hotels-g317130-Keelung-Hotels.html"],
#  ["新竹", "https://www.tripadvisor.com.tw/Hotels-g297906-Hsinchu-Hotels.html"],
#  ["苗栗", "https://www.tripadvisor.com.tw/Hotels-g616038-Miaoli-Hotels.html"]]
#  [["台中", "https://www.tripadvisor.com.tw/Hotels-g297910-Taichung-Hotels.html"]]
#彰化 雲林 嘉義
#[["台南", "https://www.tripadvisor.com.tw/Hotels-g293912-Tainan-Hotels.html"]]
#[["高雄", "https://www.tripadvisor.com.tw/Hotels-g297908-Kaohsiung-Hotels.html"]]
#[["屏東", "https://www.tripadvisor.com.tw/Hotels-g297909-Pingtung-Hotels.html"]]
#[["澎湖", "https://www.tripadvisor.com.tw/Hotels-g1437280-Penghu-Hotels.html"]]
#[["金門", "https://www.tripadvisor.com.tw/Hotels-g1152699-Kinmen-Hotels.html"]]
#[["馬祖", "https://www.tripadvisor.com.tw/Hotels-g1731586-Matsu-Hotels.html"]]
#[["台東", "https://www.tripadvisor.com.tw/Hotels-g304163-Taitung-Hotels.html"]]
#[["花蓮", "https://www.tripadvisor.com.tw/Hotels-g297907-Hualien-Hotels.html"]]
#[["宜蘭", "https://www.tripadvisor.com.tw/Hotels-g608526-Yilan-Hotels.html"]]
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test2'
)
cursor = cnx.cursor(buffered=True)
for i in range(len(target)):
    getSites(target[i][0], target[i][1])
tEnd = time.time()
print("Run Time：", tEnd - tStart)
