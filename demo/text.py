import mysql.connector
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

import pandas as pd

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

import datetime
import time
from time import sleep
driver = webdriver.Chrome("chromedriver")
url = "https://www.tripadvisor.com.tw/Attraction_Review-g13808515-d552573-Reviews-Taipei_101-Xinyi_District_Taipei.html"
driver.get(url)
try:
    Bad_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_2')]")
    webdriver.ActionChains(driver).move_to_element(
                Bad_click).click(Bad_click).perform()
except NoSuchElementException:
    print('===')
    pass

a = driver.find_element_by_xpath(
    "//input[contains(@id, 'ReviewRatingFilter_5')]").get_attribute("checked")

b = driver.find_element_by_xpath(
    "//input[contains(@id, 'ReviewRatingFilter_2')]").get_attribute("checked")

print(a)
print(b)


# cnx = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="12345678",
#     database='test1'
# )
# cursor = cnx.cursor(buffered=True)

# for each in cursor:
#     a = each[0].split(" ")
#     print(a[0])


# target = [["基隆", "https://www.tripadvisor.com.tw/Attractions-g317130-Activities-Keelung.html"],
#           ["台北", "https://www.tripadvisor.com.tw/Attractions-g293913-Activities-Taipei.html"],
#           ["新北", "https://www.tripadvisor.com.tw/Attractions-g1432365-Activities-New_Taipei.html"],
#           ["桃園", "https://www.tripadvisor.com.tw/Attractions-g297912-Activities-Taoyuan.html"],
#           ["新竹", "https://www.tripadvisor.com.tw/Attractions-g297906-Activities-Hsinchu.html"],
#           ["苗栗", "https://www.tripadvisor.com.tw/Attractions-g616038-Activities-Miaoli.html"],
#           ["台中", "https://www.tripadvisor.com.tw/Attractions-g297910-Activities-Taichung.html"],
#           ["彰化", "https://www.tripadvisor.com.tw/Attractions-g304153-Activities-Changhua.html"],
#           ["雲林", "https://www.tripadvisor.com.tw/Attractions-g616037-Activities-Yunlin.html"],
#           ["嘉義", "https://www.tripadvisor.com.tw/Attractions-g1433864-Activities-Chiayi_County.html"],
#           ["嘉義", "https://www.tripadvisor.com.tw/Attractions-g297904-Activities-Chiayi.html"],
#           ["高雄", "https://www.tripadvisor.com.tw/Attractions-g297908-Activities-Kaohsiung.html"],
#           ["屏東", "https://www.tripadvisor.com.tw/Attractions-g297909-Activities-Pingtung.html"],
#           ["台東", "https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung.html"],
#           ["花蓮", "https://www.tripadvisor.com.tw/Attractions-g297907-Activities-Hualien.html"],
#           ["宜蘭", "https://www.tripadvisor.com.tw/Attractions-g608526-Activities-Yilan.html"],
#           ["澎湖", "https://www.tripadvisor.com.tw/Attractions-g1437280-Activities-Penghu.html"],
#           ["金門", "https://www.tripadvisor.com.tw/Attractions-g1152699-Activities-Kinmen.html"],
#           ["馬祖", "https://www.tripadvisor.com.tw/Attractions-g1731586-Activities-Matsu.html"]]
