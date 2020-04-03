# -*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
from time import sleep
import re
import mysql.connector
from touringDict import touringDict

# driver = webdriver.Chrome("chromedriver")
# driver.get("https://www.tripadvisor.com.tw/Attraction_Review-g304163-d6964072-Reviews-Dapo_Pond-Taitung.html")
# driver.implicitly_wait(5)

# # Terrible_click = driver.find_element_by_xpath(
# #     "//label[contains(@for, 'ReviewRatingFilter_1')]"
# # )
# # Bad_click = driver.find_element_by_xpath(
# #     "//label[contains(@for, 'ReviewRatingFilter_2')]"
# # )
# # Normal_click = driver.find_element_by_xpath(
# #     "//label[contains(@for, 'ReviewRatingFilter_3')]"
# #)
# try:
#     Great_click = driver.find_element_by_xpath(
#         "//label[contains(@for, 'ReviewRatingFilter_5')]")
#     webdriver.ActionChains(driver).move_to_element(Great_click).click(Great_click).perform()
#     print("五星勾選")
# except NoSuchElementException:
#     try:
#         Great_click = driver.find_element_by_xpath(
#         "//label[contains(@for, 'filters_detail_checkbox_trating__5')]")
#         webdriver.ActionChains(driver).move_to_element(
#             Great_click).click(Great_click).perform()
#         print("五星勾選")
#     except NoSuchElementException:
#         print("No Great_click")
#         pass

# try:
#     Good_click = driver.find_element_by_xpath(
#         "//label[contains(@for, 'ReviewRatingFilter_4')]")
#     webdriver.ActionChains(driver).move_to_element(Good_click).click(Good_click).perform()
#     print("四星勾選")
# except NoSuchElementException:
#     try:
#         Good_click = driver.find_element_by_xpath(
#         "//label[contains(@for, 'filters_detail_checkbox_trating__4')]")
#         webdriver.ActionChains(driver).move_to_element(
#             Good_click).click(Good_click).perform()
#         print("四星勾選")
#     except NoSuchElementException:
#         print("No Great_click")
#         pass


# a = "沙雕"
# b = "不錯"
# c = "沙雕不錯"

# if c in b:
#     print("good")
# else:
#     print("nono")

# a = ["好","不好"]

# if "好" in a:
#     print("111")

# noun = "沙雕、便當、便當店、玩水、海灘、沙灘、作品、藝術、火車、大眾運輸工具、攜家帶眷、小孩、拍照、戲水、親子、館藏、展品、捷運、交通、咖啡、門票、收費、空調、冷氣、管理、模型、價格、購物、禮品、歌劇院、戲劇院、夕陽、景色、景象、觀景台、環境、標示、登山、停車、車位、太陽、垃圾、垃圾桶、指示、人、公園、土質、樹、溜滑梯、溜冰場、草地、池塘、遊樂區、河堤、遊民、景觀、噴水池、標示、夜景、設備、廁所、寺廟、夜市、美食、廟、攝影、雕塑、遊客、動物、休息、纜車、吃、規劃、購物中心、商店、郊遊、風景、溫泉、態度"

# comment = "天很適合全家一起來遊玩的地方，自己開車或是搭火車公車都可以到達，附近飲食也非常方便。 有很多家有名的便當店，可以一邊看海一邊吃午餐，如果沒有太熱感覺還不錯。 而且每年沙雕的主題都不同，所以每天都可以看到不同的沙雕。"
# lst = noun.split("、")
# b = ""
# aa = ""
# for i in range(len(comment)):
#         end = i + 7
#         if end > len(comment):
#             pass
#         else:
#             compare = comment[i:end]
#         for ss in lst:
#             if ss in compare:
#                 aa = ss
#         print(aa)

# noun = ['環境衛生設備', '保養狀況廁所', '一家大小態度', '大眾運輸工具', '停車場氣味', '步道溜滑梯', '遮避觀景台', '停車位作品', '食品選擇性', '龍舟比賽', '等待時間', '歷史背景', '硬體設備', '遊樂設施', '湖景公園', '逛街夕陽', '商城佈置', '購物中心', '整修門票', '全家大小', '攜家帶眷', '親水設施', '小吃交通', '美食餐廳', '飲食種類', '餐廳選擇', '便當店', '棒球場', '戲劇院', '歌劇院', '單車道', '垃圾桶', '哺乳室', '洗手間', '遊戲區', '遊樂區', '溜冰場', '小木屋', '櫻花樹', '噴水池', '手扶梯', '動物園', '戲水區', '停車場', '選擇性', '美食街', '燈塔', '風車', '規模', '溫泉', '纜車', '沙雕', '寺廟', '路燈', '座椅', '冷氣',
#         '空調', '氣味', '垃圾', '山路', '空氣', '登山', '綠地', '陰影', '河堤', '土質', '池塘', '草地', '風景', '夜景', '景觀', '太陽', '環境', '景象', '景色', '品牌', '電梯', '裝飾', '商店', '禮品', '購物', '價格', '收費', '動線', '服務', '標示', '指示', '規劃', '管理', '遊客', '遊民', '親子', '小孩', '野餐', '郊遊', '休息', '攝影', '拍照', '動物', '海邊', '海岸', '戲水', '沙灘', '海灘', '玩水', '雕塑', '模型', '展品', '館藏', '藝術', '會車', '動向', '路線', '車位', '停車', '捷運', '火車', '餐點', '夜市', '美食', '咖啡', '便當', '廟', '土', '樹', '人', '沙', '吃']
# aa = "又有沙雕藝術品"
# for each in noun:
#     if each in aa:
#         print(each)
# driver = webdriver.Chrome("chromedriver")
# driver.get("https://www.tripadvisor.com.tw/Hotels-g293913-Taipei-Hotels.html")
# lastPage = driver.find_element_by_xpath(
#     "//a[contains(@class, 'pageNum last ')]").get_attribute('href')
# p1_each = "//a[contains(@class, 'property_title prominent ')]"
# page = 1
# while(driver.current_url != lastPage):
#     a = driver.find_elements_by_xpath(p1_each)
#     for i in a:
#         print(i.get_attribute('href'))
#     try:
#         driver.implicitly_wait(5)
#         nextPage_url = driver.find_element_by_xpath(
#             "//a[contains(@class, 'nav next ui_button primary')]").get_attribute('href')
#         driver.get(nextPage_url)
#         page += 1
#     except NoSuchElementException:
#         break


# driver = webdriver.Chrome("chromedriver")
# driver.get("https://www.tripadvisor.com.tw/Hotel_Review-g13808853-d8555273-Reviews-Via_Hotel_Taipei_Station-Zhongzheng_District_Taipei.html")
# try:
#     page = requests.get(
#         "https://www.tripadvisor.com.tw/Hotel_Review-g13808853-d8555273-Reviews-Via_Hotel_Taipei_Station-Zhongzheng_District_Taipei.html").text
#     soup = BeautifulSoup(page, 'html.parser')
#     score = soup.find('span', 'hotels-hotel-review-about-with-photos-Reviews__overallRating--vElGA').text
#     print(score)
#     # rate = score.span['text']
#     # Rate = re.findall(r'[\d\.\d]+', rate)
#     # rate = Rate[0]
# except AttributeError:
#     rate = "None"


# page = requests.get(
#     "https://www.tripadvisor.com.tw/Hotel_Review-g13806951-d3134481-Reviews-Via_Hotel-Wanhua_Taipei.html").text
# soup = BeautifulSoup(page, 'html.parser')

# facility = soup.find_all('div', {'data-test-target': 'amenity_text'})
# for i in facility:
#     print(i.get_text())

# strr = "因為這是一個七月的周末 在沙灘上同時舉行兩個夏季節日，可以想像會有很多人吧。如果正計劃去福隆參加慶祝活動，請確保早點上火車或巴士，人很多呢!"
# print(strr.replace("七月",""))

# strip_chars = '？"。.，,《》[]〖〗“”  '
# strr = strr.translate(strr.maketrans(dict.fromkeys(strip_chars,"#")))
# sttr_lst = strr.split("#")
# for each in sttr_lst:
#     print(each)



# cnx2 = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="12345678",
#     database='test2'
# )

# sql = "SELECT id,name,city_name,address,type,comment,rate,href FROM `site_data` WHERE city_name = '台南'"
# cursor = cnx2.cursor(buffered=True)
# cursor2 = cnx.cursor(buffered=True)
# cursor.execute(sql)

# for each in cursor:
#     idid = each[0]
#     name = each[1]
#     city_name = each[2]
#     address = each[3]
#     type1 = each[4]
#     comment = each[5]
#     rate = each[6]
#     href = each[7]
#     add_data = ("INSERT INTO site_data"
#                 "(id,name,city_name,address,type,comment,rate,href) "
#                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
#     data = (idid, name, city_name, address, type1, comment, rate, href)
#     print(name)
#     cursor2.execute(add_data, data)
#     cnx.commit()

# sql = "SELECT from_id,to_id FROM `site_relationship` WHERE from_id = ANY(SELECT id FROM `site_data` WHERE city_name = '台南')"
# cursor = cnx2.cursor(buffered=True)
# cursor2 = cnx.cursor(buffered=True)
# cursor.execute(sql)

# for each in cursor:
#     from_id = each[0]
#     to_id = each[1]
#     add_data = ("INSERT INTO `site_relationship`"
#                 "(`from_id`, `to_id`) "
#                 "VALUES (%s,%s)")
#     data = (from_id, to_id)
#     print(from_id)
#     cursor2.execute(add_data, data)
#     cnx.commit()

# cnx = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="12345678",
#     database='test3',
#     buffered=True
# )

# sql = "SELECT from_id,to_id FROM `site_relationship`"
# cursor2 = cnx.cursor()
# cursor3 = cnx.cursor()
# cursor2.execute(sql)
# for each in cursor2:
#     from_id = each[0]
#     sql = "SELECT id FROM `site_data` WHERE id = '" + from_id + "'"
#     cursor3.execute(sql)
#     entry = cursor3.fetchone()
#     if entry is None:
#         print(from_id)

a = touringDict()
a.setSentence("好多洗衣機")
print(a.sentence)
c = a.getConclusion()
a.setSentence("沙雕好大")
print(a.sentence)
d = a.getConclusion()
print(c)
print(d)
