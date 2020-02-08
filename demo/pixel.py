from selenium import webdriver
import requests
import time
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup

# driver = webdriver.Chrome("chromedriver")
# driver.get("https://store.google.com/tw/config/pixel_3a")
# sleep(2)
# buttons = driver.find_elements_by_xpath("//div[contains(@class, 'mqn-lobby__card ng-scope ng-isolate-scope')]")
# for i in buttons:
#     i.click()driver.find_element_by_xpath(
# driver.find_element_by_xpath(
#     "//div[contains(@class, 'mqn-lobby__cards-container')]/div[2]/button").click()
# recent_condition = driver.find_element_by_xpath(
#     "//div[contains(@class, 'mqn-lobby__cards-container')]/div[2]/div/div[2]/div[2]/span").get_attribute('text')
# recent_condition = driver.find_element_by_xpath(
#     "//div[contains(@class, 'mqn-lobby__card__availability ng-binding mqn-lobby__card__availability--waiting-list')]").span.get_attribute('text')
# price = []
page = requests.get("https://store.google.com/tw/config/pixel_3a").text
soup = BeautifulSoup(page, 'html.parser')
recent_condition = soup.findAll('span')
for i in recent_condition:
    print(i.span.get_text(' ', strip=True))
# print(recent_condition)

# print(recent_condition)
