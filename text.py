from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from time import sleep
print("=============start=============", end='\n')
tStart = time.time()
driver = webdriver.Chrome("chromedriver")
driver.get(
    "https://www.tripadvisor.com.tw/Attractions-g293910-Activities-c57-Taiwan.html")
driver.find_element_by_xpath("//span[contains(text(),'更多')]").click()
sleep(2)
more_xpath = "//div[contains(@class, 'filter_list_1')]/div[contains(@class, 'collapse ')]/div/label/a[contains(@class, 'taLnk')]"
c_Attrs_m = driver.find_elements_by_xpath(more_xpath)
for each_m in c_Attrs_m:
    print(each_m.get_attribute('textContent'))

