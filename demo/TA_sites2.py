from selenium import webdriver
import requests
import time
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import re

#取得所有景點資訊
def getSites(url):
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
            each_Info(all_Sites)
        else:
            all_Sites = driver.find_elements_by_xpath(rest_each)
            each_Info(all_Sites)
        #點擊下一頁
        try:
            driver.implicitly_wait(5)
            next = driver.find_element_by_link_text('下一步')
            webdriver.ActionChains(driver).move_to_element(
                next).click(next).perform()
            page += 1
        except NoSuchElementException:
            break


def each_Info(all_url):
    for each in all_url:
        url = each.get_attribute('href')
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        #景點名稱
        name = " "
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
        tags = soup.find('div', 'detail').findAll('a')
        for i in tags:
            if(i.get_text() == "更多"):
                pass
            else:
                lst_tag.append(i.get_text().strip())
        print("景點名：" + name + " 分數：" + rate + " 評論數：" ,
              str(c_comment) + " 位置：" + address + " href：" + url)
    print("="*100)


#Main
tStart = time.time()
driver = webdriver.Chrome("chromedriver")
url = "https://www.tripadvisor.com.tw/Attractions-g293912-Activities-Tainan.html"
getSites(url)
tEnd = time.time()
print("Run Time：", tEnd - tStart)
