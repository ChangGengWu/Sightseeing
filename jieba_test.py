import sys
import jieba
import jieba.analyse
from selenium import webdriver
#取得第一則評論
driver =  webdriver.Chrome("chromedriver")
driver.get("https://www.mobile01.com/topicdetail.php?f=444&t=5902771")
#//div[contains(@class, 'l-content__main')]/div[4]/div[變數]/div[2]/div/article
comment = "//div[contains(@class, 'l-content__main')]/div[4]/div[4]/div[2]/div/article"
to_comment = driver.find_element_by_xpath(comment)
get_comment = to_comment.get_attribute('textContent')
fn_comment = get_comment.strip()#除去空白
print(fn_comment)
#斷句
cut_comment = jieba.cut(fn_comment,cut_all=False)
print("斷句結果：  " + "/".join(cut_comment))
#關鍵字分析
extract_cmt = jieba.analyse.extract_tags(fn_comment, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
for tag in extract_cmt:
    print("關鍵字：",tag[0],"出現頻率：",tag[1])
