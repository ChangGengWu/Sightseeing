from selenium import webdriver
import requests
import time
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import re

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.tripadvisor.com.tw/Hotels-g293910-Taiwan-Hotels.html")
show_all = driver.find_element_by_xpath(
    "//div[contains(@class, 'common-filters-FilterWrapper__container--3m4Qd')]/div[2]/div[5]/span")
show_all.click()
