from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
import datetime
import time
from time import sleep
import mysql.connector


# Main
def Main():
    "搜尋6頁好評論"
    getPositiveUser(url)
    "加入資料庫"
    dataBase()


# 取得該日打卡資訊(正評)
def getPositiveUser(url):
    pageNum = 1
    select_filter("positive")

    sleep(1)

    # 不超過6頁
    while True:
        print(pageNum)

        total = driver.find_elements_by_xpath(
            "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a"
        )

        for i in range(len(total)):
            try:
                # 使用者
                User = driver.find_elements_by_xpath(
                    "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a"
                )
                userName = User[i].get_attribute("textContent")

                try:
                    # 造訪日期
                    visit_Day = driver.find_elements_by_xpath(
                        "//div[contains(@class,'location-review-review-content-ttd-review-content-ttd__footer--VYYV8')]"
                    )
                    visitDay = visit_Day[i].get_attribute("textContent").split(" ")
                    visitDay = visitDay[1]
                    print(visitDay)
                except:
                    # 造訪日期
                    visit_Day = driver.find_elements_by_xpath(
                        "//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span"
                    )
                    visitDay = visit_Day[i].get_attribute("textContent").split("，")
                    visitDay = visitDay[1]
                    print(visitDay)

                if "Tripadvisor 會員" in userName:
                    print(userName)
                    print()
                else:
                    # 使用者
                    userName = User[i].get_attribute("textContent")
                    userHref = User[i].get_attribute("href")
                    print(userName)
                    print(userHref)

                    # 評論 && 造訪日期
                    # 搜網址
                    Comment = driver.find_elements_by_xpath(
                        "//div[contains(@class,'location-review-review-list-parts-ReviewTitle__reviewTitle--2GO9Z')]/a"
                    )
                    commentUrl = Comment[i].get_attribute("href")

                    # 搜尋個人頁面
                    page = requests.get(commentUrl).text
                    soup = BeautifulSoup(page, "html.parser")

                    # 評論
                    try:
                        userComment = soup.find("span", "fullText").get_text()
                        print(userComment)

                    except Exception as e:
                        print("喔呀")
                        print(e)
                        pass

                    # 造訪日期
                    try:
                        postDay = (
                            soup.find(
                                "div",
                                {
                                    "class": "ui_column is-10-desktop is-12-tablet is-12-mobile"
                                },
                            )
                            .find("span", {"class": "ratingDate"})
                            .get("title")
                        )
                        print(postDay)

                    except Exception as e:
                        print("啊呀")
                        print(e)
                        pass

                    if userComment == "":
                        pass
                    else:
                        Good_name.append(userName)
                        Good_href.append(userHref)
                        Good_comment.append(userComment)
                        Good_visitDay.append(visitDay)
                        Good_postDay.append(postDay)

                    print()

            except Exception as e:
                print("哎呀")
                print(e)
                pass

            sleep(1)

        # 這頁已經搜尋完畢+1
        pageNum += 1

        if pageNum > 7:
            print("好評論搜尋完畢")
            return

        try:
            nextPage = driver.find_element_by_link_text("下一步")

            webdriver.ActionChains(driver).move_to_element(nextPage).click(
                nextPage
            ).perform()
            sleep(1)
            print("下一頁了")

        except Exception as e:
            print("沒下一頁了")
            print(e)
            return


# 評等選擇器 positive/negative
def select_filter(condition):
    # 正面評等
    if condition == "positive":
        # 五星評價
        try:
            Excellent_click = driver.find_element_by_xpath(
                "//label[contains(@for, 'ReviewRatingFilter_5')]"
            )

            webdriver.ActionChains(driver).move_to_element(Excellent_click).click(
                Excellent_click
            ).perform()
            print("五星勾選")

        except NoSuchElementException:
            try:
                Excellent_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_5')]"
                )

                webdriver.ActionChains(driver).move_to_element(Excellent_click).click(
                    Excellent_click
                ).perform()
                print("五星勾選")
            except NoSuchElementException:
                print("No Excellent_click")
                pass

        # 四星評價
        try:
            Good_click = driver.find_element_by_xpath(
                "//label[contains(@for, 'ReviewRatingFilter_4')]"
            )

            webdriver.ActionChains(driver).move_to_element(Good_click).click(
                Good_click
            ).perform()
            print("四星勾選")

        except NoSuchElementException:
            try:
                Good_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_4')]"
                )

                webdriver.ActionChains(driver).move_to_element(Good_click).click(
                    Good_click
                ).perform()
                print("四星勾選")
            except NoSuchElementException:
                print("No Good_click")
                pass

    # 負面評等
    elif condition == "negative":
        # 二星評價
        try:
            Bad_click = driver.find_element_by_xpath(
                "//label[contains(@for, 'ReviewRatingFilter_2')]"
            )

            webdriver.ActionChains(driver).move_to_element(Bad_click).click(
                Bad_click
            ).perform()
            print("二星勾選")

        except NoSuchElementException:
            try:
                Bad_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_2')]"
                )

                webdriver.ActionChains(driver).move_to_element(Bad_click).click(
                    Bad_click
                ).perform()
                print("二星勾選")
            except NoSuchElementException:
                print("No Bad_click")
                pass

        # 一星評價
        try:
            Terrible_click = driver.find_element_by_xpath(
                "//label[contains(@for, 'ReviewRatingFilter_1')]"
            )

            webdriver.ActionChains(driver).move_to_element(Terrible_click).click(
                Terrible_click
            ).perform()
            print("一星勾選")

        except NoSuchElementException:
            try:
                Terrible_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_1')]"
                )

                webdriver.ActionChains(driver).move_to_element(Terrible_click).click(
                    Terrible_click
                ).perform()
                print("一星勾選")
            except NoSuchElementException:
                print("No Terrible_click")
                pass

    # 負面評價+三星評價
    elif condition == "normal":
        # 三星評價
        try:
            Normal_click = driver.find_element_by_xpath(
                "//label[contains(@for, 'ReviewRatingFilter_3')]"
            )

            webdriver.ActionChains(driver).move_to_element(Normal_click).click(
                Normal_click
            ).perform()
            print("三星勾選")

        except NoSuchElementException:
            try:
                Normal_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_3')]"
                )

                webdriver.ActionChains(driver).move_to_element(Normal_click).click(
                    Normal_click
                ).perform()
                print("三星勾選")
            except NoSuchElementException:
                print("No Normal_click")
                pass

        # 二星評價
        try:
            Bad_click = driver.find_element_by_xpath(
                "//label[contains(@for, 'ReviewRatingFilter_2')]"
            )

            webdriver.ActionChains(driver).move_to_element(Bad_click).click(
                Bad_click
            ).perform()
            print("二星勾選")

        except NoSuchElementException:
            try:
                Bad_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_2')]"
                )

                webdriver.ActionChains(driver).move_to_element(Bad_click).click(
                    Bad_click
                ).perform()
                print("二星勾選")
            except NoSuchElementException:
                print("No Bad_click")
                pass

        # 一星評價
        try:
            Terrible_click = driver.find_element_by_xpath(
                "//label[contains(@for, 'ReviewRatingFilter_1')]"
            )

            webdriver.ActionChains(driver).move_to_element(Terrible_click).click(
                Terrible_click
            ).perform()
            print("一星勾選")

        except NoSuchElementException:
            try:
                Terrible_click = driver.find_element_by_xpath(
                    "//label[contains(@for, 'ReviewRatingFilter_1')]"
                )

                webdriver.ActionChains(driver).move_to_element(Terrible_click).click(
                    Terrible_click
                ).perform()
                print("一星勾選")
            except NoSuchElementException:
                print("No Terrible_click")
                pass

    else:
        print("Error")


# 搜尋全部景點
def dbTaipei_Search():
    countSite = 1

    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database='test4'
    )
    cursor = cnx.cursor()

    # query
    target = ['H00732', 'H09870', 'H14037']
    
    for i in target:
        query = "SELECT id , name , href , city_name  FROM `hotel_data` WHERE id = '" + i + "'"
        cursor.execute(query)
        for (Sid, name, href, city_name) in cursor:
            idlst.append(Sid)
            namelst.append(name)
            hreflst.append(href)
            citylst.append(city_name)
            countSite += 1
        
    # print(Sid,href,city_name)

    # Make sure data is committed to the database
    cursor.close()
    cnx.close()

    return countSite


# 資料庫
def dataBase():

    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database='test4'
    )
    cursor = cnx.cursor()

    # Insert
    add_User = (
        "INSERT INTO hotel_comment "
        "(name,href,comment,Sid,city_name,site,evaluation,visitDay,postDay)"
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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
                Site,
                "P",
                Good_visitDay[i],
                Good_postDay[i],
            )
            cursor.execute(add_User, data_User)
            i += 1
    except:
        print("好評論匯入失敗")

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()
    print("匯入成功")


# 主運行程式
"開始"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(5)
time_start = time.time()

"執行dbTaipei_Search()並且取總筆數"
hreflst = []
namelst = []
idlst = []
citylst = []
 
# 景點數量
siteCount = dbTaipei_Search()
print(siteCount)

"搜尋各個景點的評論者"
no = 175
#1003
for cout in range(0, siteCount):
    # sleep(3)
    # 評論者名稱/網址/造訪日期/評論ß
    Good_name = []
    Good_href = []
    Good_visitDay = []
    Good_comment = []
    Good_postDay = []

    try:
        # 網址/代號/城市名
        url = hreflst[cout]
        Sid = idlst[cout]
        cityID = citylst[cout]

        "執行"

        try:
            driver.get(url)
            sleep(5)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(10)
            print("Was a nice sleep, now let me continue...")
            driver.get(url)

        # 景點名稱
        Site = namelst[cout]
        print(Site)

        Main()
            

    except Exception as e:
        print(e)
        print(cout,"程式碼有誤，跳出")

    print("第%s筆" % cout)

"結束"
time_end = time.time()
print("\n")
print(time_end - time_start)

