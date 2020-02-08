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
driver.get("https://www.tripadvisor.com.tw/Attraction_Review-g304163-d6964072-Reviews-Dapo_Pond-Taitung.html")
driver.implicitly_wait(5)

# Terrible_click = driver.find_element_by_xpath(
#     "//label[contains(@for, 'ReviewRatingFilter_1')]"
# )
# Bad_click = driver.find_element_by_xpath(
#     "//label[contains(@for, 'ReviewRatingFilter_2')]"
# )
# Normal_click = driver.find_element_by_xpath(
#     "//label[contains(@for, 'ReviewRatingFilter_3')]"
#)
try:
    Great_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_5')]")
    webdriver.ActionChains(driver).move_to_element(Great_click).click(Great_click).perform()
    print("五星勾選")
except NoSuchElementException:
    try:
        Great_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'filters_detail_checkbox_trating__5')]")
        webdriver.ActionChains(driver).move_to_element(
            Great_click).click(Great_click).perform()
        print("五星勾選")
    except NoSuchElementException:
        print("No Great_click")
        pass

try:
    Good_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'ReviewRatingFilter_4')]")
    webdriver.ActionChains(driver).move_to_element(Good_click).click(Good_click).perform()
    print("四星勾選")
except NoSuchElementException:
    try:
        Good_click = driver.find_element_by_xpath(
        "//label[contains(@for, 'filters_detail_checkbox_trating__4')]")
        webdriver.ActionChains(driver).move_to_element(
            Good_click).click(Good_click).perform()
        print("四星勾選")
    except NoSuchElementException:
        print("No Great_click")
        pass
