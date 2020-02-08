import sys
import jieba
import jieba.analyse
import mysql.connector
import re
import operator
import itertools


def config():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database='test1'
    )
    return cnx

def add_Data(cnx,id, segment, evaluation):
    cursor = cnx.cursor()
    add_data = ("INSERT INTO comment_segment"
                "(id,segment,color,shape) "
                "VALUES (%s,%s,%s,%s)")
    if(evaluation == "正面評價"):
        data = (id, segment, "green", "square")
        cursor.execute(add_data, data)
        cnx.commit()
    else:
        data = (id, segment, "red", "square")
        cursor.execute(add_data, data)
        cnx.commit()


def eval_to_color(eval):
    color = "green"
    if(eval =="p"):
        color = color
    else:
        color = "red"
    return color


def lst_stopwords():
    words = []
    #引入停用詞庫
    with open('stopwords.txt', 'r', encoding='UTF-8') as file:
        for data in file.readlines():
            data = data.strip()
            words.append(data)
    return words

def site_name_segment(cnx,site_id):
    query = "SELECT name FROM `site` WHERE id = '" + site_id + "'"
    cursor = cnx.cursor()
    cursor.execute(query)
    for ele in cursor:
        #print(ele[0])
        site_name = ele[0]
        sn_seg = []
        sn_seg = jieba.lcut(site_name, cut_all=False)
    return sn_seg

def get_all_comment(cnx,s_id):
    cursor = cnx.cursor(buffered=True)
    sql = "SELECT id,comment,evaluation FROM `user_comment` WHERE site_ID = '" + s_id + "'"
    cursor.execute(sql)
    for ele in cursor:
        c_id = ele[0]
        comment = ele[1]
        evaluation = ele[2]
        print(comment)
        #comment_seg(c_id, comment, evaluation, s_id)
        build_relationship(cnx, comment, s_id)


def comment_seg(cnx, c_id, comment, evaluation, s_id):
    cursor = cnx.cursor(buffered=True)
    sn_seg = site_name_segment(cnx, s_id)
    stopWords = lst_stopwords()
    #過濾停用詞與空格
    remainderWords = remainderWords_maker(stopWords, sn_seg, comment)
    for ele in remainderWords:
        color = eval_to_color(evaluation)
        sql = "SELECT segment,color FROM `comment_segment` WHERE segment = '"+ ele + "' AND color = '" + color + "'"
        cursor.execute(sql)
        entry = cursor.fetchone()
        if entry is None:
            id = " "
            add_Data(cnx, id, ele, evaluation)
            print("sucessful!")
        else:
            pass

def remainderWords_maker(stopWords, sn_seg, comment):
    c_cut = jieba.cut(comment, cut_all=False)
    remainderWords = list(
        filter(lambda a: a not in stopWords and a != '\n' and a not in sn_seg and a != ' ', c_cut))
    return remainderWords


def build_relationship(cnx, comment,s_id):
    cursor = cnx.cursor(buffered=True)
    sn_seg = site_name_segment(cnx, s_id)
    stopWords = lst_stopwords()
    #過濾停用詞與空格
    remainderWords = remainderWords_maker(stopWords, sn_seg, comment)
    list_of_relation = [
        (s1, s2) for s1 in remainderWords for s2 in remainderWords if s1 != s2]
    for tup in list_of_relation:
        cursor1 = cnx.cursor(buffered=True)
        cursor2 = cnx.cursor(buffered=True)
        sql = "SELECT id FROM `comment_segment` WHERE segment = '" + tup[0] + "'"
        sql_2 = "SELECT id FROM `comment_segment` WHERE segment = '" + tup[1] + "'"
        cursor1.execute(sql)
        cursor2.execute(sql_2)
        from_id = ""
        to_id = ""
        for ele in cursor1:
            from_id = ele[0]
        for elee in cursor2:
            to_id = elee[0]
        add_Relationship(cnx,from_id, to_id)
        # cursor1.close()
        # cursor2.close()


def add_Relationship(cnx,from_id, to_id):
    cursor = cnx.cursor(buffered=True)
    add_relation = ("INSERT INTO `comment_segment_relationship`"
                "(`from`, `to`) "
                "VALUES (%s,%s)")
    data = (from_id, to_id)
    cursor.execute(add_relation, data)
    cnx.commit()

def main():
    cnx = config()
    target = "S0101"
    get_all_comment(cnx, target)


main()









    # corpus += remainderWords
    # ctn += 1
    # #斷詞配對(同一則評論斷詞彼此互連)
    # list_of_relation = [(s1, s2) for s1 in remainderWords for s2 in remainderWords if s1 != s2]
    # print(ctn,list_of_relation)
    # print("====================================================")


# def seg_is_exit(seg,evluation):
#     sql = "SELECT * `user_comment` WHERE segment = " + seg + " AND e

# dic = {}
# for ele in corpus:
#     if ele not in dic:
#         dic[ele] = 1
#     else:
#         dic[ele] = dic[ele] + 1

# print("評論數共",ctn,"則")
# print("斷句" + "\t" + "出現次數")
# sort_cmt = sorted(dic.items(),key= operator.itemgetter(1),reverse = True)
# for each in sort_cmt:
#     if((len(each[0]) >= 2) and (str.isdigit(each[0]) == False)):
#         print(each[0] , "\t" , each[1])


