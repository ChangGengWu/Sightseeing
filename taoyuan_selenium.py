from selenium import webdriver
import time
import pandas as pd
print("=============start=============",end='\n')
tStart = time.time()
driver =  webdriver.Chrome("chromedriver")
driver.get("https://travel.tycg.gov.tw/zh-tw/travel")
path = "//div[contains(@class, 'row-item row-condition')]/ul/li"
driver.find_element_by_class_name('btn-show-adv').click()
driver.implicitly_wait(5)

#取得分區資訊 >> 取得所有每分區景點資訊 >> 取得每景點鄰近景點

#取得分區資訊
def get_RegionInfo():
    all_Area = driver.find_elements_by_xpath("//input[contains(@id,'region')]")
    region_data = []
    for each in all_Area:
        region_ID = each.get_attribute('id')
        region_Value = each.get_attribute('value')
        label_path = "//label[contains(@for,'" + region_ID +"' )]"
        region_Name = driver.find_element_by_xpath(label_path).get_attribute('textContent')
        region_data.append([region_ID, region_Value,region_Name])
    return region_data

    # choose_Area = "//input[contains(@id,'" + region_ID + "')]"
    # driver.find_element_by_xpath(choose_Area).click()


def getSiteInfo(region_ID, region_Value, region_Name):
    choose_Area = "//label[contains(@for,'" + region_ID + "')]"
    driver.find_element_by_xpath(choose_Area).click()
    submit_xpath = "//button[contains(@class,'btn-search-submit')]"
    driver.find_element_by_xpath(submit_xpath).click()

    path = "//ul[contains(@class, 'info-card-list mode-switch')]/li/div/a/div/h3"
    sites = driver.find_elements_by_xpath(path)
    count = 1
    for item in sites:
        text = item.text
        print(text)



#Main
lst_RegionInfo = get_RegionInfo()  # [region_ID,region_Value,region_Name]
for each in lst_RegionInfo:
    region_ID = each[0]
    region_Value = each[1]
    region_Name = each[2]
    getSiteInfo(region_ID, region_Value, region_Name)
    break
    

tEnd = time.time()
print(tEnd - tStart)
