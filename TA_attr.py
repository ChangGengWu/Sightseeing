from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
tStart = time.time()

#取得所有父類別網址
def get_AttrURL(URL):
    driver.get(URL)
    attr_info = []
    path = "//div[contains(@class, 'ap_filter_wrap filter_wrap_0 single_select')]/div[2]/div/label/a"
    all_Attrs = driver.find_elements_by_xpath(path)
    for each in all_Attrs:
        p_attr = each.get_attribute('textContent').split(" ")
        attr_url = each.get_attribute('href')
        attr_info.append([p_attr[0],attr_url])
    return attr_info

#取得每隔父類別的所有子類別
def get_ChildAttr(p_Attr,URL):
    driver.get(URL)
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_xpath("//span[contains(text(),'更多')]").click()
        xpath = "//div[contains(@class, 'filter_list_1')]/div/label/a"
        more_xpath = "//div[contains(@class, 'filter_list_1')]/div[contains(@class, 'collapse ')]/div/label/a[contains(@class, 'taLnk')]"
        c_Attrs = driver.find_elements_by_xpath(xpath)
        c_Attrs_m = driver.find_elements_by_xpath(more_xpath)
        p_a = []
        c_a = []
        for each in c_Attrs:
            attr = each.get_attribute('textContent').split(" ")
            p_a.append(p_Attr)
            c_a.append(attr[0])
            # print(p_Attr, attr[0])
        for each_m in c_Attrs_m:
            attr_2 = each_m.get_attribute('textContent').split(" ")
            p_a.append(p_Attr)
            c_a.append(attr_2[0])
            # print(p_Attr,attr_2[0])
    except NoSuchElementException:
        xpath = "//div[contains(@class, 'filter_list_1')]/div/label/a"
        c_Attrs = driver.find_elements_by_xpath(xpath)
        for each in c_Attrs:
            print(each.get_attribute('textContent'))
        pass
    return p_a,c_a

#main
driver = webdriver.Chrome("chromedriver")
url="https://www.tripadvisor.com.tw/Attractions-g293910-Activities-Taiwan.html"
lst_AttrURL = get_AttrURL(url)
p_Attr = []
c_Attr = []
for i in lst_AttrURL:
    a,b = get_ChildAttr(i[0],i[1])
    for k in range(len(a)):
        p_Attr.append(a[k])
        c_Attr.append(b[k])
id = range(1,len(p_Attr)+1)
print(len(id))
for each in range(len(p_Attr)):
    print(p_Attr[each],c_Attr[each])

df = pd.DataFrame({'id':id,'p_Attr':p_Attr,'c_Attr':c_Attr})
df.to_csv("site_Attr.csv",index = False,encoding='utf_8_sig')
