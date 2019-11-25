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
    lastPage = driver.find_elements_by_xpath(
        "//div[contains(@class, 'attractions-attraction-overview-main-Pagination__link--2m5mV')]/a")[-2].get_attribute('href')

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
        try:
            name = soup.find('h1', id='HEADING').get_text().strip()
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
            comment = soup.find('span', 'reviewCount')
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
              str(c_comment) + " 位置：" + address + " href：" + url)
    print("="*100)

def get_newID():
    last_id = ""
    query = "SELECT MAX(id) FROM site"
    cursor.execute(query)
    for id in cursor:
        num = re.findall(r'[\d\.\d]+', id[0])
        num = int(num[0]) + 1
        last_id = 'S{0:04}'.format(num)
    return last_id

#加入site資料到資料庫
def add_Data(id,name,city_name,address,type,c_cmt,rate,href):
    add_data = ("INSERT INTO site"
                "(id,name,city,address,type,comment,rate,href) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (id, name, city_name , address , type , c_cmt , rate , href)
    cursor.execute(add_data, data)
    cnx.commit()

#加入連結到資料庫
def add_Relationship(s_id,tags):
    add_data = ("INSERT INTO `relationship`"
                "(`from`, `to`) "
                "VALUES (%s,%s)")
    for i in range(len(tags)):
        query = "SELECT id FROM attr WHERE attr = '" + tags[i] +"'"
        cursor.execute(query)
        for each in cursor:
            data = (s_id, each[0])
            cursor.execute(add_data, data)
            cnx.commit()


#Main
tStart = time.time()
driver = webdriver.Chrome("chromedriver")
target = [["基隆", "https://www.tripadvisor.com.tw/Attractions-g317130-Activities-Keelung.html"],
          ["台北", "https://www.tripadvisor.com.tw/Attractions-g293913-Activities-Taipei.html"],
          ["新北", "https://www.tripadvisor.com.tw/Attractions-g1432365-Activities-New_Taipei.html"],
          ["桃園", "https://www.tripadvisor.com.tw/Attractions-g297912-Activities-Taoyuan.html"],
          ["新竹", "https://www.tripadvisor.com.tw/Attractions-g297906-Activities-Hsinchu.html"],
          ["苗栗", "https://www.tripadvisor.com.tw/Attractions-g616038-Activities-Miaoli.html"],
          ["台中", "https://www.tripadvisor.com.tw/Attractions-g297910-Activities-Taichung.html"],
          ["彰化", "https://www.tripadvisor.com.tw/Attractions-g304153-Activities-Changhua.html"],
          ["雲林", "https://www.tripadvisor.com.tw/Attractions-g616037-Activities-Yunlin.html"],
          ["嘉義", "https://www.tripadvisor.com.tw/Attractions-g1433864-Activities-Chiayi_County.html"],
          ["嘉義", "https://www.tripadvisor.com.tw/Attractions-g297904-Activities-Chiayi.html"],
          ["高雄", "https://www.tripadvisor.com.tw/Attractions-g297908-Activities-Kaohsiung.html"],
          ["屏東", "https://www.tripadvisor.com.tw/Attractions-g297909-Activities-Pingtung.html"],
          ["台東", "https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung.html"],
          ["花蓮", "https://www.tripadvisor.com.tw/Attractions-g297907-Activities-Hualien.html"],
          ["宜蘭", "https://www.tripadvisor.com.tw/Attractions-g608526-Activities-Yilan.html"],
          ["澎湖", "https://www.tripadvisor.com.tw/Attractions-g1437280-Activities-Penghu.html"],
          ["金門", "https://www.tripadvisor.com.tw/Attractions-g1152699-Activities-Kinmen.html"],
          ["馬祖", "https://www.tripadvisor.com.tw/Attractions-g1731586-Activities-Matsu.html"],
          ["南投", "https://www.tripadvisor.com.tw/Attractions-g304160-Activities-Nantou.html"]]

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test1'
)
cursor = cnx.cursor(buffered=True)
for i in range(len(target)):
    getSites(target[i][0], target[i][1])
tEnd = time.time()
print("Run Time：", tEnd - tStart)
