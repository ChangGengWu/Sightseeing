import sys
import jieba
import jieba.analyse
import mysql.connector
import re
import operator
import itertools
import jieba.posseg as pseg


# def lst_stopwords():
#     words = []
#     #引入停用詞庫
#     with open('stopwords.txt', 'r', encoding='UTF-8') as file:
#         for data in file.readlines():
#             data = data.strip()
#             words.append(data)
#     return words


# cnx = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="12345678",
#     database='test1'
#     )


# cursor = cnx.cursor(buffered=True)
# sql = "SELECT id,comment,evaluation FROM `user_comment` WHERE site_ID = 'S0101'"
# cursor.execute(sql)
# dic = {}
# stop_words = lst_stopwords()
# lst_execpt_POS = ['x', 'p', 'u', 'c', 'c', 'q', 'r', 'zg', 'm', 'y']
# for ele in cursor:
#         comment = ele[1]
#         print(comment)
#         words = pseg.lcut(comment)
#         # print(words)
#         for a, b in words:
#             # print(a,b)
#             # if((b == 'a') or (b == 'n')):
#                 # print(a, b)
#             if((b not in lst_execpt_POS)):
#                 print(a, b)
#                 if a not in dic:
#                     dic[a] = 1
#                 else:
#                     dic[a] = dic[a] + 1
#         print("====================================================================")
#         #comment_seg(c_id, comment, evaluation, s_id)

# sort_cmt = sorted(dic.items(),key= operator.itemgetter(1),reverse = True)
# for each in sort_cmt:
#     print(each[0] , "\t" , each[1])


c = jieba.cut("觀光景點")
for i in c:
    print(i)
