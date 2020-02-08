from selenium import webdriver
from bs4 import BeautifulSoup
import requests

import pandas as pd

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

import datetime
import time
from time import sleep

import mysql.connector

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)

from selenium.webdriver.support import expected_conditions

# Main
def Main():

    # 搜尋3頁好評論
    getPositiveUser(url)

    # 搜尋2頁負評論
    getNegativeUser(url)

    # 加入資料庫
    # dataBase()


# 取得該日打卡資訊(正評)
def getPositiveUser(url):
    driver.get(url)

    page = 1
    # 判斷有無下一頁
    tag = 0

    # 搜尋好評論
    select_filter("positive")
    sleep(1)

    # 不超過7頁
    while True:
        print(page)
        # 網頁有BUG得先按一次下一頁才能跑，只後有維護再修改
        while page == 1:
            try:
                nextPage = driver.find_element_by_link_text("下一步")
                webdriver.ActionChains(driver).move_to_element(nextPage).click(
                    nextPage
                ).perform()
                break
            except:
                print("只有一頁")
                tag = 1
                break

        # 使用者
        User = driver.find_elements_by_xpath(
            "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a"
        )

        for i in User:
            Good_href.append(i.get_attribute("href"))
            Good_name.append(i.get_attribute("text"))
            print(i.get_attribute("text"))

        # 評論
        Comment = driver.find_elements_by_xpath("//div[contains(@class,'cPQsENeY')]")

        for i in Comment:
            Good_comment.append(i.get_attribute("textContent"))

        # 造訪日期
        for i in range(len(User)):
            try:
                VisitDay = driver.find_elements_by_xpath(
                    "//div[contains(@class,'location-review-review-content-ttd-review-content-ttd__footer--VYYV8')]"
                )

                visit_Day = VisitDay[i].get_attribute("textContent").split(" ")
                Good_visitDay.append(visit_Day[1])
                print(visit_Day[1])

            except:
                VisitDay = driver.find_elements_by_xpath(
                    "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]"
                )

                visit_Day = VisitDay[i].get_attribute("textContent").split("，")
                Good_visitDay.append(visit_Day)
                print(visit_Day[1])

        sleep(1)

        # 這頁已經搜尋完畢+1
        page += 1

        # 下一頁
        if tag == 1:
            print("好評論搜尋完畢")
            return

        if page > 7:
            print("好評論搜尋完畢")
            return

        try:
            nextPage = driver.find_element_by_link_text("下一步")
            webdriver.ActionChains(driver).move_to_element(nextPage).click(
                nextPage
            ).perform()

        except:
            print("沒有下一頁了")
            print("好評論搜尋完畢")
            return


# 取得該日打卡資訊(負評)
def getNegativeUser(url):
    driver.get(url)
    sleep(1)

    # 取消評論
    cancel_filter_select("positive")

    print("有%s筆1,2星" % Star1_2)

    try:
        if Star1_2 >= 20:
            # 獲取負評
            select_filter("negative")
        else:
            # 獲得負評和普通評論
            select_filter("normal")
    except:
        # 獲得負評和普通評論
        select_filter("normal")

    page = 1
    # 判斷有無下一頁
    tag = 0

    # 不超過7頁
    while True:
        print(page)
        # 網頁有BUG得先按s一次下一頁才能跑，只後有維護再修改
        while page == 1:
            try:
                nextPage = driver.find_element_by_link_text("下一步")
                webdriver.ActionChains(driver).move_to_element(nextPage).click(
                    nextPage
                ).perform()
                break
            except:
                print("這只有一頁")
                tag = 1
                break

        # 使用者
        User = driver.find_elements_by_xpath(
            "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a"
        )

        for i in User:
            Bad_href.append(i.get_attribute("href"))
            Bad_name.append(i.get_attribute("text"))
            print(i.get_attribute("text"))

        # 評論
        Comment = driver.find_elements_by_xpath("//div[contains(@class,'cPQsENeY')]")

        for j in Comment:
            Bad_comment.append(j.get_attribute("textContent"))

        # 造訪日期
        for i in range(len(User)):
            try:
                VisitDay = driver.find_elements_by_xpath(
                    "//div[contains(@class,'location-review-review-content-ttd-review-content-ttd__footer--VYYV8')]"
                )

                visit_Day = VisitDay[i].get_attribute("textContent").split(" ")
                Bad_visitDay.append(visit_Day[1])
                print(visit_Day[1])

            except:
                VisitDay = driver.find_elements_by_xpath(
                    "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]"
                )

                visit_Day = VisitDay[i].get_attribute("textContent").split("，")
                Bad_visitDay.append(visit_Day)
                print(visit_Day[1])

        sleep(1)
        # 這頁已經搜尋完畢+1
        page += 1

        # 下一頁
        if tag == 1:
            print("壞評論搜尋完畢")
            return

        if page > 7:
            print("壞評論搜尋完畢")
            return

        try:
            nextPage = driver.find_element_by_link_text("下一步")
            webdriver.ActionChains(driver).move_to_element(nextPage).click(
                nextPage
            ).perform()
        except:
            print("沒有下一頁了")
            print("壞評論搜尋完畢")
            return


# 評等選擇器 positive/negative
def select_filter(condition):
    Great_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_5')]"
    )
    Good_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_4')]"
    )
    Terrible_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_1')]"
    )
    Bad_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_2')]"
    )
    Normal_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_3')]"
    )

    # 若需要正面評等
    if condition == "positive":
        # 選擇5星和4星評價
        try:
            webdriver.ActionChains(driver).move_to_element(Great_click).click(
                Great_click
            ).perform()
            print("五星勾選")

        except NoSuchElementException:
            print("No Great_click")
            pass

        try:
            webdriver.ActionChains(driver).move_to_element(Good_click).click(
                Good_click
            ).perform()
            print("四星勾選")

        except NoSuchElementException:
            print("No Good_click")
            pass

    # 若需要負面評等
    elif condition == "negative":
        # 選擇1星,2星

        # 1星
        try:
            webdriver.ActionChains(driver).move_to_element(Terrible_click).click(
                Terrible_click
            ).perform()
            print("一星勾選")

        except NoSuchElementException:
            print("No Terrible_click")
            pass

        # 2星
        try:
            webdriver.ActionChains(driver).move_to_element(Bad_click).click(
                Bad_click
            ).perform()
            print("二星勾選")

        except NoSuchElementException:
            print("No Bad_click")
            pass

    # 若需要三星評等
    elif condition == "normal":

        # 1星
        try:
            webdriver.ActionChains(driver).move_to_element(Terrible_click).click(
                Terrible_click
            ).perform()
            print("一星勾選")

        except NoSuchElementException:
            print("No Terrible_click")
            pass

        # 2星
        try:
            webdriver.ActionChains(driver).move_to_element(Bad_click).click(
                Bad_click
            ).perform()
            print("二星勾選")

        except NoSuchElementException:
            print("No Bad_click")
            pass

        # 3星
        try:
            webdriver.ActionChains(driver).move_to_element(Normal_click).click(
                Normal_click
            ).perform()
            print("三星勾選")

        except NoSuchElementException:
            print("No Normal_click")
            pass

    else:
        print("Error")


# 取消勾選器
def cancel_filter_select(condition):

    Great_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_5')]"
    )
    Good_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_4')]"
    )
    Terrible_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_1')]"
    )
    Bad_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_2')]"
    )

    # 若需要正面評等
    if condition == "positive":

        # 取消5星4星評論
        try:
            webdriver.ActionChains(driver).move_to_element(Great_click).click(
                Great_click
            ).perform()
            print("五星取消")

        except NoSuchElementException:
            print("失敗取消啦幹")
            pass

        try:
            webdriver.ActionChains(driver).move_to_element(Good_click).click(
                Good_click
            ).perform()
            print("四星取消")

        except NoSuchElementException:
            print("失敗取消啦幹")
            pass

    elif condition == "negative":
        # 取消1,2星評價
        try:
            webdriver.ActionChains(driver).move_to_element(Terrible_click).click(
                Terrible_click
            ).perform()
            print("一星取消")

        except NoSuchElementException:
            print("失敗取消啦幹")
            pass

        try:
            webdriver.ActionChains(driver).move_to_element(Bad_click).click(
                Bad_click
            ).perform()
            print("二星取消")

        except NoSuchElementException:
            print("失敗取消啦幹")
            pass

    else:
        print("都沒取消到")


# 資料庫
def dataBase():

    cnx = mysql.connector.connect(
        user="root", password="406401460", host="localhost", database="homestead"
    )

    cursor = cnx.cursor()

    # Insert
    add_User = (
        "INSERT INTO user_comment "
        "(name,href,comment,Sid,city_name,site,evaluation,visitDay)"
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    )

    try:
        # 正評價加入
        i = 0
        total = len(Good_href)
        for i in range(total):
            data_User = (
                Good_name[i],
                Good_href[i],
                Good_comment[i],
                Sid,
                cityID,
                Site[0],
                "P",
                Good_visitDay[i],
            )
            cursor.execute(add_User, data_User)
            i += 1
    except:
        print("好評論匯入失敗")

    try:
        # 負評價加入
        i = 0
        total = len(Bad_href)
        for i in range(total):
            data_User = (
                Bad_name[i],
                Bad_href[i],
                Bad_comment[i],
                Sid,
                cityID,
                Site[0],
                "N",
                Bad_visitDay[i],
            )
            cursor.execute(add_User, data_User)
            i += 1
    except:
        print("壞評論匯入失敗")

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()

    print("匯入成功")


# 搜尋全台北景點
def dbTaipei_Search():
    countSite = 1

    cnx = mysql.connector.connect(
        user="root", password="406401460", host="localhost", database="homestead"
    )

    cursor = cnx.cursor()

    # query
    query = "SELECT id , href , city_name  FROM `site_data` WHERE city_name LIKE '%台北%'"

    cursor.execute(query)

    for (Sid, href, city_name) in cursor:
        idlst.append(Sid)
        hreflst.append(href)
        citylst.append(city_name)
        countSite += 1
    # print(Sid,href,city_name)

    # Make sure data is committed to the database
    cursor.close()
    cnx.close()

    return countSite


# 開始
time_start = time.time()
# 執行dbTaipei_Search()並且取總筆數
hreflst = []
idlst = []
citylst = []

countSite = dbTaipei_Search()
print(countSite)

# 搜尋各個景點的使用者
no = 1

for cout in range(countSite):
    try:
        # 使用者評論/姓名/地點
        Good_name = []
        # 網址
        Good_href = []
        # 造訪日期
        Good_visitDay = []
        # 正評論
        Good_comment = []

        # 使用者評論/姓名/地點
        Bad_name = []
        # 網址
        Bad_href = []
        # 造訪日期
        Bad_visitDay = []
        # 負評論
        Bad_comment = []

        # 網址
        url = hreflst[cout]
        # 代號
        Sid = idlst[cout]
        # 城市名
        cityID = citylst[cout]

        # 執行
        driver.get(url)

        # 景點名稱
        Site = driver.find_element_by_xpath(
            "//h1[contains(@class,'ui_header h1')]"
        ).get_attribute("textContent")
        Site = Site.strip()
        Site = Site.split(" ")
        print(Site[0])

        # 評論數
        ComAmount = driver.find_element_by_xpath(
            "//span[contains(@class,'attractions-community-content-TabBarContent__tabCount--2hTdj')]"
        ).get_attribute("textContent")
        ComAmount = ComAmount.replace(",", "")
        ComAmount = int(ComAmount)
        print(ComAmount)

        try:
            Star2 = driver.find_elements_by_xpath(
                "//span[contains(@class,'location-review-review-list-parts-ReviewRatingFilter__row_num--3cSP7')]"
            )[3].get_attribute("textContent")
            Star2 = Star2.replace(",", "")
            # print(Star2)
        except:
            Star2 = 0

        try:
            Star1 = driver.find_elements_by_xpath(
                "//span[contains(@class,'location-review-review-list-parts-ReviewRatingFilter__row_num--3cSP7')]"
            )[4].get_attribute("textContent")
            Star1 = Star1.replace(",", "")
            # print(Star1)
        except:
            Star1 = 0

        # 相加
        try:
            Star1_2 = int(Star1) + int(Star2)
        except:

            print("我他媽加失敗啦")

        sleep(1)

        if ComAmount >= 20:

            # 執行主程式
            Main()
            no += 1

        else:
            print("小於20筆資料")
            no += 1

    except:
        no += 1
        print("程式碼有誤，跳出")

    print("第%s筆" % no)


# 結束
time_end = time.time()

print("\n")
print(time_end - time_start)

