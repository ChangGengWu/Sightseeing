from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd
tStart = time.time()

#取得所有父類別網址
def get_AttrURL(URL):
    driver.get(URL)
    attr_info = []
    path = "//div[contains(@class, 'ap_filter_wrap filter_wrap_0 single_select')]/div[2]/div/label/a"
    all_Attrs = driver.find_elements_by_xpath(path)
    for each in all_Attrs:
        p_attr = each.get_attribute('textContent')
        attr_url = each.get_attribute('href')
        attr_info.append([p_attr,attr_url])
    return attr_info

#取得每隔父類別的所有子類別
def get_ChildAttr(URL):
    driver.get(URL)
    if(driver.find_element_by_xpath("//span[contains(text(),'更多')]")):
        driver.find_element_by_xpath("//span[contains(text(),'更多')]").click()
        xpath = "//div[contains(@class, 'filter_list_1')]/div/label/a"
        c_Attrs = driver.find_elements_by_xpath(xpath)
        for each in c_Attrs:
            print(each.get_attribute('textContent'))
    else:
        xpath = "//div[contains(@class, 'filter_list_1')]/div/label/a"
        c_Attrs = driver.find_elements_by_xpath(xpath)
        for each in c_Attrs:
            print(each.get_attribute('textContent'))

#main
driver = webdriver.Chrome("chromedriver")
url="https://www.tripadvisor.com.tw/Attractions-g293910-Activities-Taiwan.html"
lst_AttrURL = get_AttrURL(url)
for i in lst_AttrURL:
    get_ChildAttr(i[1])
