# -*- coding:utf-8 -*-
import difflib
import mysql.connector
from touringDict import touringDict
import numpy as np

#建立connecter
def config():
    # cnx = mysql.connector.connect(
    #     host="140.136.155.116",
    #     user="root",
    #     passwd="sightseeing",
    #     database='homestead',
    #     buffered=True
    # )
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database='test4',
        buffered=True
    )
    return cnx

def comment_seg(cnx):
    cursor_id = cnx.cursor()
    query = "SELECT DISTINCT sid FROM `user_comment`"
    cursor_id.execute(query)
    for sid in cursor_id:
        s_id = sid[0]
        cursor_all = cnx.cursor()
        sql = "SELECT id, comment, evaluation, sid FROM `user_comment` WHERE Sid = '" + s_id + "'"
        #sql = "SELECT id, comment, evaluation, Sid FROM `hotel_comment` WHERE Sid = 'H00008'"
        cursor_all.execute(sql)
        #array that save node's value,color,weight,eval
        nodes_array = [["value", "color", 0,'eval']]
        #array that save relationships's from,to,weight
        relationships_array = [[["from", "color"], ["to", "color"]]]
        for each in cursor_all:
            result = []
            comment = each[1]
            evaluation = each[2]
            site_id = each[3]
            print("=================================================")
            print(comment)
            keyword_lst = []
            #將評論所有標點符號取代成 "#"
            strip_chars = '？"。.，,！～!~《》[]〖〗“”  )('
            comment = comment.translate(
                comment.maketrans(dict.fromkeys(strip_chars, "#")))
            #將評論以 "#" 分開
            seg_lst = comment.split("#")
            #建立touringDict() 物件
            sentence = touringDict()
            positive_seg = []
            negative_seg = []
            for seg in seg_lst:
                #set sentence to object
                sentence.setSentence(seg)
                #call object function getConclusion() to get the conclusuon of sentence
                concludsion = sentence.getConclusion()
                #call object function ifPositive() to get the index (0 = negative ,1 = positive,2 = unknown)
                color_index = sentence.ifPositive()
                color = getColor(color_index,evaluation)
                if (concludsion != None):
                    print(concludsion,color)
                    node = [concludsion,color]
                    #segment ordering
                    if (color == "green") and (node not in positive_seg):
                        positive_seg.append([concludsion,color])
                        evaluation = 'P'
                    elif (color == "#E6B7BE") and (node not in negative_seg):
                        negative_seg.append(node)
                        evaluation = 'N'
                    flag = 0
                    #node add to array,if exists,weight + 1
                    for each in nodes_array:
                        if each[0] == concludsion and  each[1] == color:
                            each[2] += 1
                            flag = 1
                            break
                    if flag == 0:nodes_array.append([concludsion,color,1,evaluation])

            for i in range(len(positive_seg) - 1):
                from_seg = positive_seg[i]
                to_seg = positive_seg[i+1]
                flag = 0
                relationships_array.append([from_seg, to_seg])
            
            for i in range(len(negative_seg) - 1):
                from_seg = negative_seg[i]
                to_seg = negative_seg[i+1]
                flag = 0
                relationships_array.append([from_seg, to_seg])

        nodes_array.pop(0)
        print(nodes_array)
        for node in nodes_array:
            idid=""
            shape = "circle"
            word = node[0]
            color = node[1]
            weight = node[2]
            evaluation = node[3]
            add_Data(cnx, idid, word, color, shape, weight,evaluation,site_id)
        relationships_array.pop(0)
        print(relationships_array)
        for relationship in relationships_array:
            from_seg = relationship[0][0]
            color = relationship[0][1]
            to_seg = relationship[1][0]
            from_id,to_id = build_relationship(cnx, from_seg, to_seg, color, site_id)
            print(from_id, to_id,color)
            weight = 1
            add_Relationship(cnx, from_id, to_id, color, weight, site_id)

        markTopTwo_nodes(cnx,s_id)
        markTopTwo_relationships(cnx,s_id)


def markTopTwo_nodes(cnx,s_id):
    cursor = cnx.cursor(buffered=True)
    cursor2 = cnx.cursor(buffered=True)
    cursor3 = cnx.cursor(buffered=True)
    sql_1 = "SELECT id,weight FROM `segment_data` WHERE site_id = '" + s_id + "' AND weight >= 2 AND evaluation = 'P' ORDER BY weight DESC LIMIT 2"
    sql_2 = "SELECT id,weight FROM `segment_data` WHERE site_id = '" + s_id + \
        "' AND weight >= 2 AND evaluation = 'N' ORDER BY weight DESC LIMIT 2"
    cursor.execute(sql_1)
    cursor3.execute(sql_2)
    counter = 0
    for rec in cursor:
        idid = rec[0]
        weight = rec[1]
        query2 = ("UPDATE segment_data"
                  " SET color=%s,weight=%s"
                  " WHERE id=%s")
        if counter == 0:
            new_weight = weight * 10
            print(weight,"------>",new_weight)
            #"#C53F52","#EDAAB3"
            data = ("#33FF66", new_weight, idid)
        else:
            new_weight = weight * 8
            print(weight, "------>", new_weight)
            data = ("#33FFCC", new_weight, idid)
        cursor2.execute(query2, data)
        cnx.commit()
        counter += 1

    counter2 = 0
    for rec in cursor3:
        idid = rec[0]
        weight = rec[1]
        query2 = ("UPDATE segment_data"
                  " SET color=%s,weight=%s"
                  " WHERE id=%s")
        if counter2 == 0:
            new_weight = weight * 10
            data = ("#C42A56", new_weight, idid)
        else:
            new_weight = weight * 8
            data = ("#D6727C", new_weight, idid)
        cursor2.execute(query2, data)
        cnx.commit()
        counter2 += 1


def markTopTwo_relationships(cnx,s_id):
    cursor = cnx.cursor(buffered=True)
    cursor2 = cnx.cursor(buffered=True)
    cursor3 = cnx.cursor(buffered=True)
    sql_1 = "SELECT from_id,to_id,site_id,weight FROM `segment_relationship` WHERE site_id = '" + \
        s_id + "' AND weight >= 2 ORDER BY weight DESC LIMIT 6"
    cursor.execute(sql_1)
    counter = 0
    for rec in cursor:
        idid = rec[2]
        from_id = rec[0]
        to_id = rec[1]
        weight = rec[3]
        new_weight = weight * 6
        print(weight,"-------->",new_weight)
        query2 = ("UPDATE segment_relationship"
                  " SET color=%s,weight=%s"
                  " WHERE from_id=%s AND to_id=%s AND site_id=%s")
        data = ("#E6790D", new_weight,from_id,to_id,idid)
        cursor2.execute(query2, data)
        cnx.commit()
        counter += 1

#add segment to database
def add_Data(cnx, new_id, segment, color, shape, weight,evaluation, site_id):
    cursor = cnx.cursor(buffered=True)
    add_data = ("INSERT INTO segment_data"
                "(id, segment, color, shape,weight,evaluation ,site_id)"
                "VALUES (NULL,%s,%s,%s,%s,%s,%s)")
    data = (segment, color, shape,weight,evaluation, site_id)
    cursor.execute(add_data, data)
    cnx.commit()

#check if relationship exist in database
def check_exist(cnx, from_id, to_id, color, site_id):
    cursor = cnx.cursor(buffered=True)
    sql = "SELECT * FROM segment_relationship WHERE from_id = '" + str(from_id) + \
        "' AND to_id = '" + str(to_id) + "' AND color = '" + \
        color + "' AND site_id = '" + site_id + "'"
    cursor.execute(sql)
    entry = cursor.fetchone()
    if entry is None:
        return False
    else:
        return True


#add relationship to database
def add_Relationship(cnx, from_id, to_id, color, weight, site_id):
    # print("正在加入", from_id, to_id)
    if_exist = check_exist(cnx, from_id, to_id, color, site_id)
    if (if_exist == True):
        print("重複")
        updateWeight(cnx, from_id, to_id, color, site_id)
    else:
        cursor = cnx.cursor()
        # print(from_id,to_id)
        add_relation = ("INSERT INTO `segment_relationship`"
                        "(from_id, to_id,color,weight ,site_id) "
                        "VALUES (%s,%s,%s,%s,%s)")
        data = (from_id, to_id, color, weight, site_id)
        cursor.execute(add_relation, data)
        cnx.commit()

def getColor(index,eval):
    #0 = negative ,1 = positive,2 = unknown
    color = "green"
    if(index == 1):
        color = color
    elif(index == 0):
        color = "#E6B7BE"
    elif(index == 2):
        if(eval == "P"):
            color = color
        else:
            color = "#E6B7BE"
    return color


def updateWeight(cnx, from_id, to_id, color, site_id):
    sql = "SELECT weight FROM segment_relationship WHERE from_id = '" + str(from_id) + \
        "' AND to_id = '" + str(to_id) + "' AND color = '" + \
        color + "' AND site_id = '" + site_id + "'"
    cursor = cnx.cursor()
    cursor2 = cnx.cursor()
    cursor.execute(sql)
    weight = 0
    for res in cursor:
        weight = res[0]
    weight +=1
    query2 = ("UPDATE segment_relationship"
              " SET weight=%s"
              " WHERE site_id=%s AND from_id=%s AND to_id=%s AND color=%s")
    data = (weight,site_id,from_id,to_id,color)
    cursor2.execute(query2, data)
    cnx.commit()
    

#bulid relationship (red to red) (green to green) in each comment
def build_relationship(cnx, from_seg, to_seg, color, site_id):
    cursor1 = cnx.cursor(buffered=True)
    cursor2 = cnx.cursor(buffered=True)
    sql = "SELECT id FROM `segment_data` WHERE segment = '" + \
        from_seg + "' AND color = '" + color + "'"
    sql_2 = "SELECT id FROM `segment_data` WHERE segment = '" + \
        to_seg + "' AND color = '" + color + "'"
    cursor1.execute(sql)
    cursor2.execute(sql_2)
    from_id = ""
    to_id = ""
    for ele in cursor1:
        from_id = ele[0]
    for elee in cursor2:
        to_id = elee[0]
    return from_id,to_id

def main():
    cnx = config()
    comment_seg(cnx)

main()
