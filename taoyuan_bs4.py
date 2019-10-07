from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd
tStart = time.time()

def get_Sites(URL):
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')

    #景點名稱
    sites = soup.findAll('h3', 'info-title')
    #開放時間
    open_status = soup.find('p', 'opening-status open')
    #景點地址
    #景點評等
    #觀看數
    #print(open_status)
    id = 1
    lst_Sites = []
    lst_ID = []
    for each in sites:
        site = each.text
        lst_Sites.append(site)
        lst_ID.append(id)
        print(id, site)
        id += 1
    return lst_Sites, lst_ID
    for each in open_status:
        status = each.text
        print(status)


url = 'https://travel.tycg.gov.tw/zh-tw/travel'
site,id = get_Sites(url)

#輸出為csv檔
df = pd.DataFrame({'id': id,
                   'site_name': site})
df.to_csv("site_ID.csv", index=False, encoding='utf_8_sig')
tEnd = time.time()
print("Run Time：",tEnd - tStart)

