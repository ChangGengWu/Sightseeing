# -*- coding:utf-8 -*-
import difflib
import mysql.connector
from touringDict import touringDict

#建立connecter


def config():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database='test3',
        buffered=True
    )
    return cnx


def comment_seg(cnx):
    cursor_all = cnx.cursor()
    # sql = "SELECT id, comment, evaluation, Sid FROM `user_comment` WHERE Sid = 'S2601'"
    sql = "SELECT id, comment, evaluation, Sid FROM `hotel_comment` WHERE Sid = 'H00008'"
    cursor_all.execute(sql)
    for each in cursor_all:
        result = []
        comment = each[1]
        evaluation = each[2]
        site_id = each[3]
        # color = eval_to_color(evaluation)
        print("=================================================")
        print(comment)
        keyword_lst = []
        strip_chars = '？"。.，,！～!~《》[]〖〗“”  )('
        comment = comment.translate(
            comment.maketrans(dict.fromkeys(strip_chars, "#")))
        seg_lst = comment.split("#")
        sentence = touringDict()
        positive_seg = []
        negative_seg = []
        for seg in seg_lst:
            sentence.setSentence(seg)
            conclude = sentence.getConclusion()
            color = "green" if sentence.ifPositive() else "red"
            if (conclude != None):
                if (color == "green") and (conclude not in positive_seg):
                    positive_seg.append(conclude)
                elif (color == "red") and (conclude not in negative_seg):
                    negative_seg.append(conclude)
            else:
                pass
        keyword_lst.append(positive_seg)
        keyword_lst.append(negative_seg)
        print(keyword_lst)
        ct = 0
        for pn_lst in keyword_lst:
            color = "green" if ct == 0 else "red"
            shape = "circle"
            idid = ""
            ct += 1
            for word in pn_lst:
                print(word, color)
                add_Data(cnx, idid, word, color, shape, site_id)
            build_relationship(cnx, pn_lst, color, site_id)
        # for word in keyword_lst:
        #     shape = "circle"
        #     idid = ""
        #     add_Data(cnx, idid, word, color, shape, site_id)
        # build_relationship(cnx, keyword_lst, color, site_id)

#add segment to database
def add_Data(cnx, new_id, segment, color, shape, site_id):
    cursor = cnx.cursor(buffered=True)
    if_exist = check_exist(cnx, segment, color, site_id)
    if (if_exist == True):
        pass
    else:
        add_data = ("INSERT INTO h_segment_data"
                    "(id, segment, color, shape, hotel_id)"
                    "VALUES (%s,%s,%s,%s,%s)")
        data = (new_id, segment, color, shape, site_id)
        cursor.execute(add_data, data)
        cnx.commit()

#check if segment exist in database
def check_exist(cnx, segment, color, site_id):
    cursor = cnx.cursor(buffered=True)
    sql = "SELECT id FROM h_segment_data WHERE segment = '" + segment + \
        "' AND color = '" + color + "' AND hotel_id = '" + site_id + "'"
    cursor.execute(sql)
    entry = cursor.fetchone()
    if entry is None:
        return False
    else:
        return True

#add relationship to database
def add_Relationship(cnx, from_id, to_id, site_id):
    cursor = cnx.cursor()
    add_relation = ("INSERT INTO `h_segment_relationship`"
                    "(from_id, to_id, hotel_id) "
                    "VALUES (%s,%s,%s)")
    data = (from_id, to_id, site_id)
    cursor.execute(add_relation, data)
    cnx.commit()


def eval_to_color(eval):
    color = "green"
    if(eval == "P"):
        color = color
    else:
        color = "red"
    return color

#bulid relationship (red to red) (green to green) in each comment
def build_relationship(cnx, keyword_lst, color, site_id):
    for i in range(len(keyword_lst) - 1):
        print(keyword_lst[i], color)
        cursor1 = cnx.cursor(buffered=True)
        cursor2 = cnx.cursor(buffered=True)
        sql = "SELECT id FROM `h_segment_data` WHERE segment = '" + \
            keyword_lst[i] + "' AND color = '" + color + "'"
        sql_2 = "SELECT id FROM `h_segment_data` WHERE segment = '" + \
            keyword_lst[i+1] + "' AND color = '" + color + "'"
        cursor1.execute(sql)
        cursor2.execute(sql_2)
        from_id = ""
        to_id = ""
        for ele in cursor1:
            from_id = ele[0]
        for elee in cursor2:
            to_id = elee[0]
        add_Relationship(cnx, from_id, to_id, site_id)


def main():
    cnx = config()
    comment_seg(cnx)


main()
