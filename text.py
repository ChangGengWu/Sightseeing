from selenium import webdriver
import time
import pandas as pd
print("=============start=============", end='\n')
tStart = time.time()
driver = webdriver.Chrome("chromedriver")
driver.get(
    "https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung.html")
# seemore = "//span[contains(@class, 'ui_icon single-chevron-down single-chevron-down')]"
# driver.find_element_by_xpath(seemore).click()
# a = driver.find_element_by_link_text('下一步')
# print(a)
while True:
    seemore = "//span[contains(@class, 'ui_icon single-chevron-down single-chevron-down')]"
    try:
        driver.find_element_by_xpath(seemore).click()
        if(driver.find_element_by_link_text('下一步')):
            driver.find_element_by_link_text('下一步').click()
        else:
            break
    except:
        if(driver.find_element_by_link_text('下一步')):
            driver.find_element_by_link_text('下一步').click()
        else:
            break
