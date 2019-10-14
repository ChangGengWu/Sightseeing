from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_SiteURL(URL):
    driver.get(URL)
    driver.implicitly_wait(5)
    site_info = []
    seemore = "//span[contains(@class, 'ui_icon single-chevron-down single-chevron-down')]"
    driver.find_element_by_xpath(seemore).click()
    page1_xpath = "//div[contains(@class, 'attractions-attraction-overview-pois-PoiGrid__wrapper--2H3Mo')]/li/div[2]/div/div[2]/a"
    while True:
        all_URLs = driver.find_elements_by_xpath(page1_xpath)
        for each in all_URLs:
            site_Name = each.get_attribute('textContent')
            site_URL = each.get_attribute('href')
            site_info.append([site_Name, site_URL])
            # print(site_Name, site_URL)
        try:
            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            #     (By.LINK_TEXT,"下一步"))).click()
            driver.implicitly_wait(10)
            driver.find_element_by_link_text('下一步').click()
            xpath = "//div[contains(@class, 'tracking_attraction_title listing_title')]/a"
        except NoSuchElementException:
            break
    print(len(site_info))
        # return site_info

def get_SiteInfo(lst):
    count = 1
    print(len(lst))
    # for each in lst:
    #     url = each[1]
    #     print(each[0],each[1])
        # driver.get(url)
        # site_name = driver.find_element_by_id('HEADING').get_attribute('textContent')
        # score = driver.find_element_by_xpath(
        #     "//span[contains(@class, 'overallRating')]").get_attribute('textContent')
        # comment = driver.find_element_by_xpath(
        #     "//span[contains(@class, 'reviewCount')]").get_attribute('textContent')
        # address = driver.find_element_by_xpath(
        #     "//span[contains(@class, 'street-address')]").get_attribute('textContent')
        # print(site_name,score,comment,address)



            


# main
driver = webdriver.Chrome("chromedriver")
url = "https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung.html"
get_SiteURL(url)
#get_SiteInfo(lst)
