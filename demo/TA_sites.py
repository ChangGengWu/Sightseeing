from selenium import webdriver
import requests
import time
from time import sleep
import pandas as pd
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

#取得所有景點資訊


def getSites(url):
    driver.get(url)
    driver.implicitly_wait(5)
    seemore_xpath = "//span[contains(@class, 'ui_icon single-chevron-down single-chevron-down')]"
    driver.find_element_by_xpath(seemore_xpath).click()
    #其他頁與第一頁內容不同
    p1_xpath = "//a[contains(@class, 'attractions-attraction-overview-pois-PoiInfo__name--SJ0a4')]"
    otherpage_xpath = xpath = "//div[contains(@class, 'tracking_attraction_title listing_title')]/a"
    #確認最後一頁作為終止點
    lastPage = driver.find_elements_by_xpath(
        "//div[contains(@class, 'attractions-attraction-overview-main-Pagination__link--2m5mV')]/a")[-2].get_attribute('href')
    page = 1
    lst_Name = []
    lst_Score = []
    lst_Comment = []
    lst_Address = []
    lst_Tag = []
    #當搜尋到最後一頁stop
    while(driver.current_url != lastPage):
        if(page == 1):
                all_Sites = driver.find_elements_by_xpath(p1_xpath)
        else:
                all_Sites = driver.find_elements_by_xpath(otherpage_xpath)
        for i in range(len(all_Sites)):
                #呼叫each_info()抓取每個景點內容
                if(page == 1):
                        try:
                                site_Name, score, comment, site_Address, site_Tags = each_Info(
                                    i, p1_xpath)
                                lst_Name.append(site_Name)
                                lst_Score.append(score)
                                lst_Comment.append(comment)
                                lst_Address.append(site_Address)
                                lst_Tag.append(site_Tags)
                        except StaleElementReferenceException:
                                pass
                else:
                        try:
                                site_Name, score, comment, site_Address, site_Tags = each_Info(
                                    i, otherpage_xpath)
                                lst_Name.append(site_Name)
                                lst_Score.append(score)
                                lst_Comment.append(comment)
                                lst_Address.append(site_Address)
                                lst_Tag.append(site_Tags)
                        except StaleElementReferenceException:
                                pass
        #點擊下一頁
        try:
                if(page == 1):
                        seemore_xpath = "//span[contains(@class, 'ui_icon single-chevron-down single-chevron-down')]"
                        driver.find_element_by_xpath(seemore_xpath).click()
                        driver.find_element_by_link_text('下一步').click()
                        page += 1
                else:
                        driver.find_element_by_link_text('下一步').click()
                        page += 1
        except NoSuchElementException:
                return lst_Name, lst_Score, lst_Comment, lst_Address, lst_Tag
                break


def each_Info(index, xpath):
        #取得每個景點在list中位置
        each = driver.find_elements_by_xpath(xpath)[index]
        #前往該景點網址
        driver.get(each.get_attribute('href'))
        #宣告所有Info抓取路徑
        score_xpath = "//span[contains(@class, 'overallRating')]"
        comment_xpath = "//span[contains(@class, 'reviewCount')]"
        address_xpath = "//span[contains(@class, 'textAlignWrapper address')]/span[2]/span"
        tags_xpath = "//span[contains(@class, 'is-hidden-mobile header_detail attractionCategories')]/div/a"
        try:
                site_Name = driver.find_element_by_id(
                    'HEADING').get_attribute('textContent')
                address = driver.find_elements_by_xpath(address_xpath)
                tags = driver.find_elements_by_xpath(tags_xpath)
                try:
                        score = driver.find_element_by_xpath(
                            score_xpath).get_attribute('textContent')
                except NoSuchElementException:
                        score = "None"
                try:
                        comment = driver.find_element_by_xpath(
                            comment_xpath).get_attribute('textContent')
                except NoSuchElementException:
                        comment = "None"
                site_Address = ""
                site_Tags = ""
                lst_Addr = []
                for addr in address:
                        lst_Addr.append(addr.get_attribute('textContent'))
                site_Address = " ".join(lst_Addr)
                lst_Tags = []
                for tag in tags:
                        lst_Tags.append(tag.get_attribute('textContent'))
                site_Tags = " ".join(lst_Tags)
                driver.back()
                print("景點名：" + site_Name + " 分數：" + score + " 評論數：" +
                      comment + " 位置：" + site_Address + " 分類：" + site_Tags)
                return site_Name, score, comment, site_Address, site_Tags
        except NoSuchElementException:
                pass
        print("="*100)


#Main
tStart = time.time()
driver = webdriver.Chrome("chromedriver")
url = "https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung.html"
lst_Name, lst_Score, lst_Comment, lst_Address, lst_Tag = getSites(url)
lst_Id = []
for i in range(len(lst_Name)):
        num = '{0:03}'.format(i)
        S_id = "TD"+num
        lst_Id.append(S_id)
df = pd.DataFrame({'id': lst_Id, 'site_name': lst_Name,
                   'site_address': lst_Address, 'comments': lst_Comment, 'tags': lst_Tag})
df.to_csv("site_Data_t.csv", index=False, encoding='utf_8_sig')
tEnd = time.time()
print("Run Time：", tEnd - tStart)
