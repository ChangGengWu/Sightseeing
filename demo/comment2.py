from selenium import webdriver
from bs4 import BeautifulSoup
import requests

import pandas as pd

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

import datetime
import time
from time import sleep

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
url = "https://www.tripadvisor.com.tw/Attraction_Review-g13808515-d552573-Reviews-Taipei_101-Xinyi_District_Taipei.html"
driver.get(url)
while True:
    try:
        next = driver.find_element_by_link_text('下一步')
        webdriver.ActionChains(driver).move_to_element(next).click(next).perform()

        User = driver.find_elements_by_xpath("//div[contains(@class,'social-member-event-MemberEventOnObjectBlock__event_type--3njyv')]/span/a")
        for i in User:
            print(i.get_attribute('text'))
        print("------")
    except NoSuchElementException:
        break
