from selenium import webdriver
from bs4 import BeautifulSoup
import requests

import pandas as pd

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

import datetime
import time
from time import sleep

#取得該日打卡資訊

#取得正面評價
def getPositiveUser(url):
    driver.get(url)
    select_filter("positive")
    page = 1
    #不超過第三頁
    while(page <= 3):
        FakeUser = 'TripAdvisor 會員'.strip()
        User = driver.find_elements_by_xpath(
        "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a")
        for i in User:
            if(i.get_attribute('text').strip() == FakeUser):
                continue
            else:
                print(i.get_attribute('text'))
                print(i.get_attribute('href'))
                User_lst.append(i.get_attribute('href'))
        next_page_clicker()
        sleep(1)
        page += 1

#取得負面評價
def getNegativeUser(url):
    driver.get(url)
    cancel_filter_select()
    select_filter("negative")
    page = 1
    #不超過第二頁
    while(page <= 2):
        FakeUser = 'TripAdvisor 會員'.strip()
        User = driver.find_elements_by_xpath(
        "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a")
        for i in User:
            print(i.get_attribute('text'))
            if(i.get_attribute('text').strip() == FakeUser):
                continue
            else:
                #print(i.get_attribute('text'))
                print(i.get_attribute('href'))
                User_lst.append(i.get_attribute('href'))
        next_page_clicker()
        sleep(1)
        page += 1

#下一頁點擊器
def next_page_clicker():
    try:
        next = driver.find_element_by_link_text('下一步')
        webdriver.ActionChains(driver).move_to_element(next).click(next).perform()
    except NoSuchElementException:
        print("Error")

# def getUser():
#     FakeUser = 'TripAdvisor 會員'.strip()
#     User = driver.find_elements_by_xpath(
#             "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a")
#     for i in User:
#         if(i.get_attribute('text').strip() == FakeUser):
#             continue
#         else:
#             print(i.get_attribute('text'))
#             User_lst.append(i.get_attribute('href'))

#評等選擇器 positive/negative
def select_filter(condition):
    sleep(2)
    #若需要正面評等
    if(condition == "positive"):
        #選擇5星和4星評價
        try:
            Great_click = driver.find_element_by_xpath("//label[contains(@for, 'ReviewRatingFilter_5')]")
            webdriver.ActionChains(driver).move_to_element(
                Great_click).click(Great_click).perform()
            #若沒被成功勾選則再做一次
            if(driver.find_element_by_xpath("//input[contains(@id, 'ReviewRatingFilter_5')]").get_attribute("checked") == None):
                print("not being select!")
                Great_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_5')]")
                webdriver.ActionChains(driver).move_to_element(
                Great_click).click(Great_click).perform()
        except NoSuchElementException:
            print('===')
            pass
        try:
            Good_click = driver.find_element_by_xpath("//label[contains(@for, 'ReviewRatingFilter_4')]")
            webdriver.ActionChains(driver).move_to_element(
            Good_click).click(Good_click).perform()
            #若沒被成功勾選則再做一次
            if(driver.find_element_by_xpath("//input[contains(@id, 'ReviewRatingFilter_4')]").get_attribute("checked") == None):
                print("not being select!")
                Terrible_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_4')]")
                webdriver.ActionChains(driver).move_to_element(
                    Terrible_click).click(Terrible_click).perform()
        except NoSuchElementException:
            print('===')
            pass
    #若需要負面評等
    elif(condition == "negative"):
        #選擇1星和2星評價
        try:
            Terrible_click = driver.find_element_by_xpath("//label[contains(@for, 'ReviewRatingFilter_1')]")
            webdriver.ActionChains(driver).move_to_element(
                Terrible_click).click(Terrible_click).perform()
            #若沒被成功勾選則再做一次
            if(driver.find_element_by_xpath("//input[contains(@id, 'ReviewRatingFilter_1')]").get_attribute("checked") == None):
                print("not being select!")
                Terrible_click = driver.find_element_by_xpath(
                                "//label[contains(@for, 'ReviewRatingFilter_1')]")
                webdriver.ActionChains(driver).move_to_element(Terrible_click).click(Terrible_click).perform()
            else:
                pass
        except NoSuchElementException:
            print('===')
            pass
        try:
            Bad_click = driver.find_element_by_xpath("//label[contains(@for, 'ReviewRatingFilter_2')]")
            webdriver.ActionChains(driver).move_to_element(
                Bad_click).click(Bad_click).perform()
            #若沒被成功勾選則再做一次
            if(driver.find_element_by_xpath("//input[contains(@id, 'ReviewRatingFilter_2')]").get_attribute("checked") == None):
                print("not being select!")
                Terrible_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_2')]")
                webdriver.ActionChains(driver).move_to_element(
                    Terrible_click).click(Terrible_click).perform()
            else:
                pass
        except NoSuchElementException:
            print('===')
            pass
    else:
        print("Error")

#取消勾選器
def cancel_filter_select():
    #取消5星4星評論
    try:
        Great_click = driver.find_element_by_xpath(
            "//label[contains(@for, 'ReviewRatingFilter_5')]")
        webdriver.ActionChains(driver).move_to_element(
            Great_click).click(Great_click).perform()
        #若沒被成功取消則再做一次
        if(driver.find_element_by_xpath("//input[contains(@id, 'ReviewRatingFilter_5')]").get_attribute("checked") == True):
            print("not being canel!")
            Terrible_click = driver.find_element_by_xpath("//label[contains(@for, 'ReviewRatingFilter_5')]")
            webdriver.ActionChains(driver).move_to_element(Terrible_click).click(Terrible_click).perform()
        else:
            pass
    except NoSuchElementException:
        print('===')
        pass
    try:
        Good_click = driver.find_element_by_xpath("//label[contains(@for, 'ReviewRatingFilter_4')]")
        webdriver.ActionChains(driver).move_to_element(Good_click).click(Good_click).perform()
        #若沒被成功取消則再做一次
        if(driver.find_element_by_xpath("//input[contains(@id, 'ReviewRatingFilter_4')]").get_attribute("checked") == True):
            print("not being canel!")
            Terrible_click = driver.find_element_by_xpath(
                "//label[contains(@for, 'ReviewRatingFilter_4')]")
            webdriver.ActionChains(driver).move_to_element(
                Terrible_click).click(Terrible_click).perform()
        else:
            pass
    except NoSuchElementException:
        print('===')
        pass


#Main
#開始
time_start = time.time()

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
#使用者評論
User_lst = []
#搜尋3頁好評論
url = "https://www.tripadvisor.com.tw/Attraction_Review-g13808515-d552573-Reviews-Taipei_101-Xinyi_District_Taipei.html"
getPositiveUser(url)
#搜尋2頁負評論
getNegativeUser(url)


'''
#進入評論網址
date = '2018年1月11日'
getInformation(url,date) 
'''
for j in User_lst:
    print(j)

#結束
time_end = time.time()

print(time_end-time_start)










'''
JASONKAN
BOSS ZOE
Alfa Ren
Café.植咖啡.Espresso.コーヒー*手沖*Ice Coffee*黑咖啡
come
m791123
Café.植咖啡.Espresso.コーヒー*手沖*Ice Coffee*黑咖啡
嫻雅 王
yuen235
AnhBeer
come
ky1638
昱仁 陳
333
Apple�
cicisu
come
JASONKAN
BOSS ZOE
Erica W
Alfa Ren
come
竹北Mouette
Anita Huang
chinghs33975
Raku1088
Yali Chen
come
https://www.tripadvisor.com.tw/Profile/JASONKAN1122
https://www.tripadvisor.com.tw/Profile/BoardingPass624869
https://www.tripadvisor.com.tw/Profile/AlfaTravel666
https://www.tripadvisor.com.tw/Profile/ZhiCafe
https://www.tripadvisor.com.tw/Profile/m791123
https://www.tripadvisor.com.tw/Profile/ZhiCafe
https://www.tripadvisor.com.tw/Profile/Scenic759900
https://www.tripadvisor.com.tw/Profile/yuen235
https://www.tripadvisor.com.tw/Profile/AnhBeer
https://www.tripadvisor.com.tw/Profile/ky1638
https://www.tripadvisor.com.tw/Profile/Cosmopolitan664110
https://www.tripadvisor.com.tw/Profile/Laurent9266
https://www.tripadvisor.com.tw/Profile/applelee0313
https://www.tripadvisor.com.tw/Profile/cicisu4
https://www.tripadvisor.com.tw/Profile/JASONKAN1122
https://www.tripadvisor.com.tw/Profile/BoardingPass624869
https://www.tripadvisor.com.tw/Profile/EricaW1239
https://www.tripadvisor.com.tw/Profile/AlfaTravel666
https://www.tripadvisor.com.tw/Profile/oiseaumer
https://www.tripadvisor.com.tw/Profile/704anitah
https://www.tripadvisor.com.tw/Profile/chinghs33975
https://www.tripadvisor.com.tw/Profile/Raku1088
https://www.tripadvisor.com.tw/Profile/jasmineyali
'''
