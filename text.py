from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import re
import requests
print("=============start=============", end='\n')
# for id in range(100):
#         num = '{0:04}'.format(id)
#         print("TD"+num)

# num = 'TD{0:04}'.format(100)
# print(num)

# ss = ["ss","s111"]
# q = "INSERT INTO relationship""(from,to) ""VALUES (111, 222)"
# print(q)
# a = re.findall(r'[\d\.\d]+', num)
# print(int(a[0]))


page = requests.get(
    "https://www.tripadvisor.com.tw/Attraction_Review-g13806951-d12105255-Reviews-Nishi_Honganji_Square-Wanhua_Taipei.html").text
soup = BeautifulSoup(page, 'html.parser')
lst_tag = []
name = soup.find('h1', id='HEADING').get_text().strip()
print(name)








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
          ["馬祖", "https://www.tripadvisor.com.tw/Attractions-g1731586-Activities-Matsu.html"]]
