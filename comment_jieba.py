import sys
import jieba
import jieba.analyse
import mysql.connector
import re
import operator

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test1'
)
cursor = cnx.cursor(buffered=True)
cursur2 = cnx.cursor()

stopWords = []
#引入停用詞庫
with open('stopwords.txt', 'r', encoding='UTF-8') as file:
    for data in file.readlines():
        data = data.strip()
        stopWords.append(data)

query = "SELECT COMMENT FROM `user_comment` WHERE site_ID = 'S0101' AND evaluation = '正面評價'"
query2 = "SELECT name FROM `site` WHERE id = 'S0101'"
cursor.execute(query)
cursur2.execute(query2)

site_name = ""
for ele in cursur2:
    site_name = ele[0]
sn_seg = []
sn_seg = jieba.lcut(site_name, cut_all=False)
corpus = []
ctn = 0
for cmt in cursor:
    #print(cmt[0])
    temp = []
    c_cut = jieba.cut(cmt[0],cut_all=False)
    #過濾停用詞與空格
    remainderWords = list(
        filter(lambda a: a not in stopWords and a != '\n' and a not in sn_seg, c_cut))
    corpus += remainderWords
    ctn += 1
    for k in remainderWords:
        print(k,end=" ")
    print("")


dic = {}
for ele in corpus:
    if ele not in dic:
        dic[ele] = 1
    else:
        dic[ele] = dic[ele] + 1

print("評論數共",ctn,"則")
print("斷句" + "\t" + "出現次數")
sort_cmt = sorted(dic.items(),key= operator.itemgetter(1),reverse = True)
for each in sort_cmt:
    if((len(each[0]) >= 2) and (str.isdigit(each[0]) == False)):
        print(each[0] , "\t" , each[1])
