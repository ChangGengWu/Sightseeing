import sys
import jieba
import jieba.analyse
import mysql.connector
import re
import operator
import itertools
import jieba.posseg as pseg
'''
Process
建立connecter
====斷詞處理==== 
=> 抓評論 
=> 過濾 1.stopwords 2.POS 3.景點名
=> 加入資料庫
====連結處理====
=> 抓取斷詞ID
=> 建立relationship(ABC => A->B->C)
=> 加入資料庫
'''

#建立connecter
def config():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database='test1'
    )
    return cnx

#斷詞處理
def comment_to_seg_relationship(cnx):
    #get_comment
    cursor = cnx.cursor(buffered=True)
    sql = "SELECT id,comment,evaluation,site,Sid FROM `user_comment` WHERE Sid = 'S0101'"
    cursor.execute(sql)
    #id,comment,evaluation
    for each in cursor:
        c_id = each[0]
        cmt = each[1]
        evaluation = each[2]
        site_name = each[3]
        site_id = each[4]
        #評論,景點名斷詞
        comment_seg = pseg.lcut(cmt)
        sitename_seg = jieba.lcut(site_name, cut_all=False)
        sitename_to_jieba(cnx, site_id)
        #評論斷詞過濾
        print(cmt)
        final_seg = seg_filter(comment_seg, sitename_seg)  # return list
        seg_to_database(cnx,final_seg,evaluation,site_id)
        add_build_relationship(cnx, final_seg, evaluation,site_id)


#過濾
def seg_filter(cmt_seg,sn_seg):
    comment_seg = cmt_seg
    #stopwords
    lst_stopwords = stopwords()
    #site_name
    sitename_seg = sn_seg
    # print(sitename_seg)
    #POS
    remain_seg = []
    lst_execpt_POS = ['a', 'ad', 'ag', 'an', 'n', 'ng',
                      'nr', 'nrfg', 'nrt', 'ns', 'nt', 'nz', 'i', 'l']
    for seg,pos in comment_seg:
        if(pos in lst_execpt_POS):
            # print(seg,pos)
            remain_seg.append([seg,pos])
    # print(remain_seg)
    #remainderWords = list(
        # filter(lambda a: (a[0] not in lst_stopwords) and (a[0] != '\n') and (a[0] not in sitename_seg) and (a[0] != ' '), remain_seg))
    remainderWords = list(
        filter(lambda a: (a[0] not in lst_stopwords) and (a[0] != '\n') and (a[0] != ' '), remain_seg))
    print(remainderWords)
    return remainderWords

def sitename_to_jieba(cnx,sid):
    cursor = cnx.cursor()
    #SELECT name FROM `site` WHERE id = 'S0101'
    sql = "SELECT name FROM `site` WHERE id = '" + sid + "'"
    site_name = ""
    cursor.execute(sql)
    for ele in cursor:
        site_name = ele[0]
    jieba.add_word(site_name ,tag='n')

#stopwords
def stopwords():
    words = []
    #引入停用詞庫
    with open('stopwords.txt', 'r', encoding='UTF-8') as file:
        for data in file.readlines():
            data = data.strip()
            words.append(data)
    return words

#斷詞加入資料庫
def seg_to_database(cnx,seg,evaluation,sid):
    segment = seg
    color = eval_to_color(evaluation)
    cursor = cnx.cursor()
    cursor2 = cnx.cursor()
    for each_seg in segment:
        sql = "SELECT segment,color FROM `comment_segment1` WHERE segment = '" + each_seg[0] + "' AND color = '" + color + "'"
        cursor.execute(sql)
        entry = cursor.fetchone()
        #確認是否已存在
        if entry is None:
            add_data = ("INSERT INTO comment_segment1"
                    "(id,segment,pos,color,shape) "
                        "VALUES (%s,%s,%s,%s,%s)")
            id = ""
            data = (id, each_seg[0],each_seg[1], color, "square")
            cursor2.execute(add_data, data)
            cnx.commit()
            print("sucessful!")
        else:
            print("fail!")
            pass
        #site與seg關聯
        cursor3 = cnx.cursor(buffered=True)
        cursor5 = cnx.cursor(buffered=True)
        sql2 = "SELECT id FROM `comment_segment1` WHERE segment = '" + \
            each_seg[0] + "' AND color = '" + color + "'"
        cursor3.execute(sql2)
        #確認該斷詞id
        seg_id = ""
        for segment_id in cursor3:
            seg_id = segment_id[0]
        sql3 = "SELECT seg_id FROM `site_segment` WHERE seg_id = '" + \
            str(seg_id) + "' AND site_id = '" + sid + "'"
        cursor5.execute(sql3)
        entry2 = cursor5.fetchone()
        #若該斷詞在該景點中不存在
        if entry2 is None:
            cursor4 = cnx.cursor()
            add_data = ("INSERT INTO site_segment"
                "(site_id, seg_id) "
                "VALUES (%s,%s)")
            data = (sid,seg_id)
            cursor4.execute(add_data, data)
            cnx.commit()
        else:
            pass

def eval_to_color(eval):
    color = "green"
    if(eval == "P"):
        color = color
    else:
        color = "red"
    return color

#建立斷詞關聯


def add_build_relationship(cnx, seg_lst, evaluation, s_id):
    cursor1 = cnx.cursor(buffered=True)
    cursor2 = cnx.cursor(buffered=True)
    site_id = s_id
    color = eval_to_color(evaluation)
    seg = seg_lst
    #抓seg_lst各斷詞id
    print(seg)
    a_pos = []
    n_pos = []
    for each in seg:
        if('a' in each[1]):
            a_pos.append(each[0])
        else:
            n_pos.append(each[0])
    for a_seg in a_pos:
        for n_seg in n_pos:
            from_seg = a_seg
            to_seg = n_seg
            print("關係：",a_seg,n_seg)
            sql_1 = "SELECT id FROM `comment_segment1` WHERE segment = '" + \
                from_seg + "' AND color = '" + color + "'"
            sql_2 = "SELECT id FROM `comment_segment1` WHERE segment = '" + \
                 to_seg + "' AND color = '" + color + "'"
            cursor1.execute(sql_1)
            cursor2.execute(sql_2)
            from_id = ""
            to_id = ""
            for ele in cursor1:
                from_id = ele[0]
            for elee in cursor2:
                to_id = elee[0]
            print(from_id, to_id)
            add_Relationship(cnx, from_id, to_id,site_id)
    
    # for i in range(len(seg) - 1):
    #     from_seg = seg[i]
    #     to_seg = seg[i+1]
    #     #SELECT * FROM `comment_segment` WHERE `segment` = '地方' AND color = 'red'
    #     sql_1 = "SELECT id FROM `comment_segment` WHERE segment = '" + from_seg + "' AND color = '" + color + "'"
    #     sql_2 = "SELECT id FROM `comment_segment` WHERE segment = '" + \
    #         to_seg + "' AND color = '" + color + "'"
        # cursor1.execute(sql_1)
        # cursor2.execute(sql_2)
        # from_id = ""
        # to_id = ""
        # for ele in cursor1:
        #     from_id = ele[0]
        # for elee in cursor2:
        #     to_id = elee[0]
        # add_Relationship(cnx, from_id, to_id)


def add_Relationship(cnx, from_id, to_id,sid):
    cursor = cnx.cursor(buffered=True)
    print(from_id,to_id)
    add_relation = ("INSERT INTO `comment_segment_relationship1`"
                    "(`from`, `to`,`site_id`) "
                    "VALUES (%s,%s,%s)")
    data = (from_id, to_id,sid)
    cursor.execute(add_relation, data)
    cnx.commit()


    #相連
    #加入資料庫

def main():
    cnx = config()
    comment_to_seg_relationship(cnx)  # return seg_lst site_id
    # add_build_relationship(seg_lst)

main()
