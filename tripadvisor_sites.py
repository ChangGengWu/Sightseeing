from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


def get_SiteURL(URL):
    driver.get(URL)
    seemore = "//span[contains(@class, 'ui_icon single-chevron-down single-chevron-down')]"
    driver.find_element_by_xpath(seemore).click()
    xpath = "//div[contains(@class, 'attractions-attraction-overview-pois-PoiGrid__wrapper--2H3Mo')]/li/div[2]/div/div[2]/a"
    while True:
        all_URLs = driver.find_elements_by_xpath(xpath)
        for each in all_URLs:
            site_Name = each.get_attribute('textContent')
            site_URL = each.get_attribute('href')
            print(site_Name, site_URL)
        try:
            driver.find_element_by_link_text('下一步').click()
            driver.implicitly_wait(2)
            xpath = "//div[contains(@class, 'tracking_attraction_title listing_title')]/a"
        except NoSuchElementException:
            break

            


# main
driver = webdriver.Chrome("chromedriver")
url = "https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung.html"
get_SiteURL(url)
