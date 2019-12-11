from selenium import webdriver
from bs4 import BeautifulSoup
import requests

import pandas as pd

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

import datetime
import time
from time import sleep

import mysql.connector

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)

#Main
def Main():

    #搜尋3頁好評論
    getPositiveUser(url)

    #搜尋2頁負評論
    driver.get(url)
    getNegativeUser(url)

    #加入資料庫
    # dataBase()

#取得該日打卡資訊(正評)


def getPositiveUser(url):

    #選擇5星和4星評價
    try:
        Great_click = driver.find_element_by_xpath(
            "//label[contains(@for, 'ReviewRatingFilter_5')]")
        Great_click.click()

        Good_click = driver.find_element_by_xpath(
            "//label[contains(@for, 'ReviewRatingFilter_4')]")
        Good_click.click()

    except NoSuchElementException:
        print('false')
        pass

    #搜尋好評論
    FakeUser = 'TripAdvisor 會員'.strip()
    page = 1

    #不超過第三頁
    while(True):

        #print(page)
        #網頁有BUG得先按一次下一頁才能跑，只後有維護再修改
        if(page == 1):
            driver.find_element_by_link_text('下一步').click()

        User = driver.find_elements_by_xpath(
            "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a")

        for i in User:
            if(i.get_attribute('text').strip() == FakeUser):
                continue
            else:
                User_lst.append(i.get_attribute('href'))
                Name_lst.append(i.get_attribute('text'))

        sleep(1)
        #這頁已經搜尋完畢+1
        page += 1

        #下一頁
        if(page > 3):
            break
        else:
            try:
                driver.find_element_by_link_text('下一步').click()
            except NoSuchElementException:
                print('end')
                break

#取得該日打卡資訊(負評)


def getNegativeUser(url):

    #取消5星4星評論
    Great_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_5')]").click()
    Good_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_4')]").click()

    #選擇1星和2星評價
    try:
        Terrible_click = driver.find_element_by_xpath(
            "//label[contains(@for, 'ReviewRatingFilter_1')]")
        Terrible_click.click()

        Bad_click = driver.find_element_by_xpath(
            "//label[contains(@for, 'ReviewRatingFilter_2')]")
        Bad_click.click()

    except NoSuchElementException:
        print('false')
        pass

      #搜尋好評論
    FakeUser = 'TripAdvisor 會員'.strip()
    page = 1

    #不超過第三頁
    while(True):

        #print(page)
        #網頁有BUG得先按一次下一頁才能跑，只後有維護再修改
        if(page == 1):
            driver.find_element_by_link_text('下一步').click()

        User = driver.find_elements_by_xpath(
            "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a")

        for i in User:
            if(i.get_attribute('text').strip() == FakeUser):
                continue
            else:
                User_lst.append(i.get_attribute('href'))
                Name_lst.append(i.get_attribute('text'))

        sleep(1)
        #這頁已經搜尋完畢+1
        page += 1

        #下一頁
        if(page > 2):
            break
        else:
            try:
                driver.find_element_by_link_text('下一步').click()
            except NoSuchElementException:
                print('end')
                break

#資料庫


# def dataBase():

#     cnx = mysql.connector.connect(user='root',
#                                   password='406401460',
#                                   host='localhost',
#                                   database='homestead')

#     cursor = cnx.cursor()

#     # Insert
#     add_User = (
#         "INSERT INTO user_comment " "(name,href,site) " "VALUES (%s,%s,%s)")

#     i = 0
#     total = len(Name_lst)
#     for i in range(total):
#         data_User = (Name_lst[i], User_lst[i], Site)
#         cursor.execute(add_User, data_User)
#         i += 1

#     # Make sure data is committed to the database
#     cnx.commit()
#     cursor.close()
#     cnx.close()


#開始
time_start = time.time()

#使用者評論/姓名/地點
Name_lst = []
User_lst = []
url = "https://www.tripadvisor.com.tw/Attraction_Review-g13808515-d552573-Reviews-Taipei_101-Xinyi_District_Taipei.html"

#景點名稱
driver.get(url)
Site = driver.find_element_by_xpath(
    "//li[contains(@class,'breadcrumb')]").get_attribute('textContent')
print(Site.strip())

#執行主程式
Main()

#印出所有資料
i = 0
total = len(Name_lst)
for i in range(total):
    print(Name_lst[i])
    print(User_lst[i])
    i += 1

#結束
time_end = time.time()

print('\n')
print(time_end-time_start)
