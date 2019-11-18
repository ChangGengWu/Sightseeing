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
    name = soup.find('h1', id='HEADING').get_text()
    print(name)
    #開放時間
    # open_status = soup.find('p', 'opening-status open')
    #景點地址
    address = soup.find('span', 'textAlignWrapper address').get_text()
    print(address)
    #景點評等
    try:
        info = soup.find('div', 'ratingContainer')
        A = info.span['alt']
    except AttributeError:
        print("None")
    #評論數
    try:
        comment = soup.find('span', 'reviewCount')
        print(comment.get_text())
    except AttributeError:
        print("None")
    #類別
    tags = soup.find('div', 'detail').findAll('a')
    # try:
    #     more_tags = soup.find('span', 'collapse hidden').findAll('a')
    #     print(more_tags.text)
    #     for j in more_tags:
    #         print(j.get_text())
    # except AttributeError:
    #     pass
    
    # for i in tags:
    #     if(i.get_text() == "更多"):
    #         pass
    #     else:
    #         print(i.get_text())
    #print(open_status)
    # id = 1
    # lst_Sites = []
    # lst_ID = []
    # for each in sites:
    #     site = each.text
    #     lst_Sites.append(site)
    #     lst_ID.append(id)
    #     print(id, site)
    #     id += 1
    # return lst_Sites, lst_ID
    # for each in open_status:
    #     status = each.text
    #     print(status)


url = 'https://www.tripadvisor.com.tw/Attraction_Review-g304163-d8639453-Reviews-Lvdaoshilang-Taitung.html'
get_Sites(url)

#輸出為csv檔
# df = pd.DataFrame({'id': id,
#                    'site_name': site})
# df.to_csv("site_ID.csv", index=False, encoding='utf_8_sig')
tEnd = time.time()
print("Run Time：",tEnd - tStart)

