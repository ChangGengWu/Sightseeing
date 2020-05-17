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
import numpy as np

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
a.setSentence("小孩有趣")
# print(a.sentence)
b = a.getConclusion()
# c = a.getNoun()
# d = a.getClassification()
# e = a.getAdj()
# print(c)
# print(e)
print(b)
# print(d)
# a = [['夜景評價好的', 'green'], ['親子推薦前往', 'green'], 1]
# v = "b"
# clr = "red"
# print(a[0][1])
# from_id = 1
# to_id = 2
# color = "green"
# site_id = 'S0101'
# sql = "SELECT * FROM segment_relationship WHERE from_id = '" + str(from_id) + \
#     "' AND to_id = '" + str(to_id) + "' AND color = '" + \
#     color + "' AND site_id = '" + site_id + "'"
# print(sql)

# cnx = mysql.connector.connect(
#         host="140.136.155.116",
#         user="root",
#         passwd="sightseeing",
#         database='homestead',
#         buffered=True
#     )

# cnx = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="12345678",
#     database='test4',
#     buffered=True
# )
# cursor = cnx.cursor()
# cursor2 = cnx.cursor()

# all_lst = []
# ids = []

# query = "Select DISTINCT Sid FROM user_comment"
# cursor.execute(query)
# for each in cursor:
#     ids.append(each[0])
    
# query2 = "Select id FROM site_data WHERE comment>30"
# cursor2.execute(query2)
# for rec in cursor2:
#     all_lst.append(rec[0])

# target = []
# for i in all_lst:
#     if i not in ids:
#         print(i)
#         target.append(i)
# print(target)

# human = ["人", "小孩", "老人", "小朋友", "老年人", "身障者", "年長者", "年長的人", "遊客", "親子", "遊民", "一家大小"]

# classification = ['便宜','昂貴', '美麗', '不好看', '好吃', '難吃', '無趣', '炎熱', '寒冷', '乾淨', '髒亂'
#                   '遙遠', '難找', '擁擠', '寧靜', '熱鬧', '舒適', '方便', '評價好的', '評價差的', '有趣', '簡陋', '老舊', '完善', '適中', '一般', '新穎', '豐盛', '豪華', '久']

# lst_dict = []
# with open('dict.txt', 'r', encoding='UTF-8', errors='ignore') as f:
#         for data in f.readlines():
#                 lst_dict.append(data.strip())

# cb = []
# for h in human:
#         for c in classification:
#                 st = h+c
#                 cb.append(st)

# print(len(lst_dict))
# for each in cb:
#         if each in lst_dict:
#                 lst_dict.remove(each)
                
# print(len(lst_dict))

# classification_for_human = ['覺得便宜', '覺得昂貴', '覺得美麗', '覺得不好看', '覺得好吃', '覺得難吃', '覺得無趣', '覺得炎熱', '覺得寒冷', '覺得乾淨', '覺得髒亂'
#                             '覺得遙遠', '覺得難找', '覺得擁擠', '覺得寧靜', '覺得熱鬧', '覺得舒適', '覺得不清楚', '覺得評價好的', '覺得評價差的', '覺得有趣', '覺得簡陋', '覺得老舊', '覺得完善', '覺得一般', '覺得新穎', '覺得豐盛', '覺得豪華']
# for h in human:
#         for c in classification_for_human:
#                 st = h+c
#                 lst_dict.append(st)

# print(len(lst_dict))

# with open('dict2.txt', 'w') as f:
#        for item in lst_dict:
#                f.write("%s\n" % item)
# if '一家大小無趣' in lst_dict:
#         print('true')
#        for conclude in classification:
#               for each in noun:
#                      item = each + conclude
#                      f.write("%s\n" % item)
#                      print(item)


# def getClassification(noun,adjs):
#         human = ["人", "小孩", "老人", "小朋友", "老年人", "身障者",
#                  "年長者", "年長的人", "遊客", "親子", "遊民", "一家大小"]
#         many = ['種類多', '有點多', '多到爆', '非常多', '蠻多', '超多',
#                 '很多', '許多', '滿滿', '不少', '多', '大量', '豐富', '多']
#         few = ['沒有很多', '有點少', '非常少', '超少', '蠻少', '很少', '較少', '不多', '少']
#         big = ['蠻大的', '巨大', '超大', '很大', '大', '寬敞']
#         small = ['有點小', '蠻小的', '蠻小', '很小', '窄小', '小']
#         high = ['高', '不低']
#         low = ['低', '不高']
#         inexpensive = ['很實惠', '便宜', '實惠', '平價', '低廉', '合理', '親民']
#         free = ['不用錢', '免費']
#         expensive = ['蠻貴的', '不便宜', '蠻貴', '超貴', '很貴', '貴']
#         beautiful = ['美麗的', '漂亮的', '好美', '美', '精緻',
#                      '栩栩如生', '鬼斧神工', '精美', '壯觀', '雅緻', '漂亮', '美麗']
#         ugly = ['難看', '醜']
#         delicious = ['好吃', "美味", '美食']
#         yucky = ['不好吃', '難吃']
#         wonderful = ['厲害', '細膩', '用心', '驚喜', '很棒', '強大']
#         boring = ['無聊', '無趣']
#         interesting = ['有趣', '好玩', '開心']
#         clean = ['整潔', '乾淨']
#         mess = ['不乾淨', '骯髒', '亂', '髒']
#         convenient = ['超方便', '便利', '方便']
#         inconvenient = ['相當不便', '不方便', '不便', '塞車']
#         insufficient = ['不太足夠', '不足夠', '不夠', '不足', '不齊全', '不全']
#         sufficient = ['齊全', '足夠的', '足夠', '夠']
#         good_manner = ['有耐心', '有禮貌', '態度好', '和善',
#                        '用心', '親切', '友善', '熱心', '專業', '細心', '周到', '誠懇']
#         bad_manner = ['態度很差', '態度差', '沒禮貌', '不和善',
#                       '沒耐心', '沒耐性', '傲慢', '兇', '愛理不理', '不耐煩', '冷淡']
#         far = ['路途遙遠', '遙遠', '遠', '不近']
#         close = ['鄰近', '近', '不遠']
#         recommend = ['推薦', '喜歡', '適合', '值得']
#         hard_to_find = ['非常難找', '難求', '一位難求']
#         many_people = ['擁擠', '紊亂', '擠']
#         quient = ['寧靜', '安靜', '平靜']
#         lively = ['熱鬧']
#         comfortable = ['更舒服', '舒適', '新鮮', '明亮', '優美', '舒服']
#         blurry = ['不夠清楚', '不夠簡單', '有落差', '不清楚', '複雜', '不易']
#         good = ['最棒的', '特別好', '沒話說', '良好', '優秀',
#                 '好', '棒', '好', '優', '佳', '沒話說', '不錯', '印象深刻', '嘆為觀止', '讚嘆', '震撼']
#         bad = ['不是特別好', '非常不好', '美中不足', '再加強', '不理想', '不建議', '沒品質', '不值得',
#                '詭異', '害怕', '危險', '掃興', '差勁', '不推', '糟糕', '爛', '不良', '不佳', '失望', '不適合', '不是很好']
#         have = ['有', '具備']
#         no_have = ['沒有', '不具備', '沒']
#         not_stable = ['不太穩定', '不穩定']
#         stable = ['穩定']
#         elses = ['簡陋', '有力', '異常', '迅速', '老舊', '完善',
#                  '適中', '一般', '新穎', '豐盛', '豪華', '怪', '軟', '久', '慢', '硬']
#         conclusion = ""
#         if(adjs in many):
#             conclusion = "多"
#         elif(adjs in few):
#             conclusion = "少"
#         elif(adjs in big):
#             conclusion = "大"
#         elif(adjs in small):
#             conclusion = "小"
#         elif(adjs in inexpensive):
#             if noun in human:
#                 conclusion = "覺得便宜"
#             else:
#                 conclusion = "便宜"
#         elif(adjs in free):
#             conclusion = "免費"
#         elif(adjs in expensive):
#             if noun in human:
#                 conclusion = "覺得昂貴"
#             else:
#                 conclusion = "昂貴"
#         elif(adjs in beautiful):
#             if noun in human:
#                 conclusion = "覺得美麗"
#             else:
#                 conclusion = "美麗"
#         elif(adjs in ugly):
#             if noun in human:
#                 conclusion = "覺得不好看"
#             else:
#                 conclusion = "不好看"
#         elif(adjs in delicious):
#             if noun in human:
#                 conclusion = "覺得好吃"
#             else:
#                 conclusion = "好吃"
#         elif(adjs in yucky):
#             if noun in human:
#                 conclusion = "覺得難吃"
#             else:
#                 conclusion = "難吃"
#         elif(adjs in wonderful):
#             conclusion = "值得一看"
#         elif(adjs in boring):
#             if noun in human:
#                 conclusion = "覺得無趣"
#             else:
#                 conclusion = "無趣"
#         # elif(adjs in hot):
#         #     if noun in human:
#         #         conclusion = "覺得炎熱"
#         #     else:
#         #         conclusion = "炎熱"
#         # elif(adjs in cold):
#         #     if noun in human:
#         #         conclusion = "覺得寒冷"
#         #     else:
#         #         conclusion = "寒冷"
#         elif(adjs in clean):
#             if noun in human:
#                 conclusion = "覺得乾淨"
#             else:
#                 conclusion = "乾淨"
#         elif(adjs in mess):
#             if noun in human:
#                 conclusion = "覺得髒亂"
#             else:
#                 conclusion = "髒亂"
#         elif(adjs in convenient):
#             if noun in human:
#                 conclusion = "覺得方便"
#             else:
#                 conclusion = "方便"
#         elif(adjs in inconvenient):
#             if noun in human:
#                 conclusion = "覺得不方便"
#             else:
#                 conclusion = "不方便"
#         elif(adjs in insufficient):
#             conclusion = "不足"
#         elif(adjs in good_manner):
#             conclusion = "態度優良"
#         elif(adjs in bad_manner):
#             conclusion = "態度不佳"
#         elif(adjs in far):
#             if noun in human:
#                 conclusion = "覺得遙遠"
#             else:
#                 conclusion = "遙遠"
#         elif(adjs in recommend):
#             conclusion = "推薦前往"
#         elif(adjs in hard_to_find):
#             if noun in human:
#                 conclusion = "覺得難找"
#             else:
#                 conclusion = "難找"
#         elif(adjs in many_people):
#             if noun in human:
#                 conclusion = "覺得擁擠"
#             else:
#                 conclusion = "擁擠"
#         elif(adjs in quient):
#             if noun in human:
#                 conclusion = "覺得寧靜"
#             else:
#                 conclusion = "寧靜"
#         elif(adjs in lively):
#             if noun in human:
#                 conclusion = "覺得熱鬧"
#             else:
#                 conclusion = "熱鬧"
#         elif(adjs in comfortable):
#             if noun in human:
#                 conclusion = "覺得舒適"
#             else:
#                 conclusion = "舒適"
#         elif(adjs in blurry):
#                 conclusion = "不清楚"
#         elif(adjs in good):
#             if noun in human:
#                 conclusion = "覺得評價好的"
#             else:
#                 conclusion = "評價好的"
#         elif(adjs in bad):
#             if noun in human:
#                 conclusion = "覺得評價差的"
#             else:
#                 conclusion = "評價差的"
#         elif (adjs in elses):
#             if noun in human:
#                 conclusion = "覺得" + adjs
#             else:
#                 conclusion = adjs
#         elif (adjs in close):
#             conclusion = "鄰近"
#         elif (adjs in sufficient):
#             conclusion = "齊全"
#         elif (adjs in high):
#             conclusion = "高"
#         elif (adjs in low):
#             conclusion = "低"
#         elif (adjs in interesting):
#             if noun in human:
#                 conclusion = "覺得有趣"
#             else:
#                 conclusion = "有趣"
#         elif (adjs in have):
#             conclusion = "具備"
#         elif (adjs in no_have):
#             conclusion = "不具備"
#         elif (adjs in stable):
#             conclusion = "穩定"
#         elif (adjs in not_stable):
#             conclusion = "不穩定"
#         return conclusion


# a = getClassification("小孩","有趣")
# print(a)