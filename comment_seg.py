# -*- coding:utf-8 -*-
import difflib
import mysql.connector
from touringDict import touringDict
import numpy as np

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
    sql = "SELECT id, comment, evaluation, Sid FROM `user_comment` WHERE Sid = 'S0102'"
    #sql = "SELECT id, comment, evaluation, Sid FROM `hotel_comment` WHERE Sid = 'H00008'"
    cursor_all.execute(sql)
    #array that save node's value,color,weight
    nodes_array = [["value", "color", 0]]
    #array that save relationships's from,to,weight
    relationships_array = [[["from", "color"], ["to", "color"], 0]]
    for each in cursor_all:
        result = []
        comment = each[1]
        evaluation = each[2]
        site_id = each[3]
        print("=================================================")
        # print(comment)
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
                elif (color == "red") and (node not in negative_seg):
                    negative_seg.append(node)
                flag = 0
                #node add to array,if exists,weight + 1
                for each in nodes_array:
                    if each[0] == concludsion and  each[1] == color:
                        each[2] += 1
                        flag = 1
                        break
                if flag == 0:nodes_array.append([concludsion,color,1])

        for i in range(len(positive_seg) - 1):
            from_seg = positive_seg[i]
            to_seg = positive_seg[i+1]
            flag = 0
            for each in relationships_array:
                # print(each[0][0], from_seg)
                #如果from to 值相同且顏色同為綠色 weight+1
                if(each[0] == from_seg and each[1] == to_seg) or (each[1] == from_seg and each[0] == to_seg):
                    # print(each[0], each[1], each[2])
                    each[2] += 1
                    flag = 1
                    break
            if flag == 0:
                relationships_array.append([from_seg, to_seg, 1])
        
        for i in range(len(negative_seg) - 1):
            from_seg = negative_seg[i]
            to_seg = negative_seg[i+1]
            flag = 0
            for each in relationships_array:
                # print(each[0][0], from_seg)
                #如果from to 值相同且顏色同為綠色 weight+1
                if(each[0] == from_seg and each[1] == to_seg) or (each[1] == from_seg and each[0] == to_seg):
                    # print(each[0], each[1], each[2])
                    each[2] += 1
                    flag = 1
                    break
            if flag == 0:
                relationships_array.append([from_seg, to_seg, 1])
    
    # for node in nodes_array:
    #     idid=""
    #     shape = "circle"
    #     word = node[0]
    #     color = node[1]
    #     weight = node[2]
    #     add_Data(cnx, idid, word, color, shape, weight,site_id)
    for relationship in relationships_array:
        from_id = relationship[0][0]
        color = relationship[0][1]
        to_id = relationship[1][0]
        weight = 1
        add_Relationship(cnx, from_id, to_id, color, weight, site_id)


#add segment to database
def add_Data(cnx, new_id, segment, color, shape, weight, site_id):
    cursor = cnx.cursor(buffered=True)
    # if_exist = check_exist(cnx,segment, color, site_id)
    # if (if_exist == True):
    #     pass
    # else:
    add_data = ("INSERT INTO segment_data"
                "(id, segment, color, shape,weight, site_id)"
                "VALUES (%s,%s,%s,%s,%s,%s)")
    data = (new_id, segment, color, shape,weight, site_id)
    cursor.execute(add_data, data)
    cnx.commit()

#check if segment exist in database
def check_exist(cnx, from_id, to_id, color, site_id):
    cursor = cnx.cursor(buffered=True)
    sql = "SELECT * FROM segment_relationship WHERE from_id = '" + from_id + \
        "' AND to_id = '" + to_id + "' AND color = '" + \
        color + "' AND site_id = '" + site_id + "'"
    cursor.execute(sql)
    entry = cursor.fetchone()
    if entry is None:
        return False
    else:
        return True


#add relationship to database
def add_Relationship(cnx, from_id, to_id, color, weight, site_id):
    if_exist = check_exist(cnx, from_id, to_id, color, site_id)
    if (if_exist == True):
        updateWeight(cnx, from_id, to_id, color, site_id)
    else:
        cursor = cnx.cursor()
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
        color = "red"
    elif(index == 2):
        if(eval == "P"):
            color = color
        else:
            color = "red"
    return color


def updateWeight(cnx, from_id, to_id, color, site_id):
    sql = "SELECT weight FROM segment_relationship WHERE from_id = '" + from_id + \
        "' AND to_id = '" + to_id + "' AND color = '" + \
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
# def build_relationship(cnx,keyword_lst, color, site_id):
#     for i in range(len(keyword_lst) - 1):
#         print(keyword_lst[i], color)
#         cursor1 = cnx.cursor(buffered=True)
#         cursor2 = cnx.cursor(buffered=True)
#         sql = "SELECT id FROM `segment_data` WHERE segment = '" + \
#             keyword_lst[i] + "' AND color = '" + color + "'"
#         sql_2 = "SELECT id FROM `segment_data` WHERE segment = '" + \
#             keyword_lst[i+1] + "' AND color = '" + color + "'"
#         cursor1.execute(sql)
#         cursor2.execute(sql_2)
#         from_id = ""
#         to_id = ""
#         for ele in cursor1:
#             from_id = ele[0]
#         for elee in cursor2:
#             to_id = elee[0]
#         add_Relationship(cnx,from_id, to_id, site_id)

def main():
    cnx = config()
    comment_seg(cnx)

main()


   # max_weight = 1
   # second_weight = 1
# max_index = 0
# second_index = 0
# for j in range(len(nodes_array)):
#     print(nodes_array[j][0],nodes_array[j][2])
#     if nodes_array[j][2] > max_weight:
#         max_weight = nodes_array[j][2]
#         max_index = j
#     elif(nodes_array[j][2] > second_weight and nodes_array[j][2] < max_weight):
#         second_weight = nodes_array[j][2]
#         second_index = j
# print(nodes_array[max_index][0],max_weight)
# print(nodes_array[second_index][0], second_weight)
# for relationship in relationships_array:
#     print(relationship)

# if (concludsion != None):
#     if (color == "green") and (concludsion not in positive_seg):
#         positive_seg.append(concludsion)
#     elif (color == "red") and (concludsion not in negative_seg):
#         negative_seg.append(concludsion)
# else:
#     pass
# keyword_lst.append(positive_seg)
# keyword_lst.append(negative_seg)
# print(keyword_lst)
# ct = 0
# for pn_lst in keyword_lst:
#     color = "green" if ct == 0 else "red"
#     shape = "circle"
#     idid = ""
#     ct += 1
#     for word in pn_lst:
#         print(word,color)
#     add_Data(cnx, idid, word, color, shape, site_id)
# build_relationship(cnx, pn_lst, color, site_id)
# for word in keyword_lst:
#     shape = "circle"
#     idid = ""
#     add_Data(cnx, idid, word, color, shape, site_id)
# build_relationship(cnx, keyword_lst, color, site_id)

#change max,second weight color
# def changeMaxTwoNodeColor(nodes_array):
#     max_weight = 1
#     second_weight = 1
#     max_index = 0
#     second_index = 0

#     max_weight_N = 1
#     second_weight_N = 1
#     max_index_N = 0
#     second_index_N = 0
#     for j in range(len(nodes_array)):
#         if(nodes_array[j][1] == 'green'):
#             if nodes_array[j][2] > max_weight:
#                 max_weight = nodes_array[j][2]
#                 max_index = j
#             elif(nodes_array[j][2] > second_weight and nodes_array[j][2] < max_weight):
#                 second_weight = nodes_array[j][2]
#                 second_index = j
#         if(nodes_array[j][1] == 'red'):
#             if nodes_array[j][2] > max_weight_N:
#                 max_weight_N = nodes_array[j][2]
#                 max_index_N = j
#             elif(nodes_array[j][2] > second_weight_N and nodes_array[j][2] < max_weight_N):
#                 second_weight_N = nodes_array[j][2]
#                 second_index_N = j
#     nodes_array[max_index][1] = "orange"
#     nodes_array[second_index][1] = "orange"
#     nodes_array[max_index_N][1] = "orange"
#     nodes_array[second_index_N][1] = "orange"
#     print("正面前二：", nodes_array[max_index][0], nodes_array[second_index][0])
#     print("負面前二：", nodes_array[max_index_N][0], nodes_array[second_index_N][0])
#     return nodes_array

# #change max,second weight color
# def changeMaxTwoRelationColor(relationships_array):
#     max_weight = 1
#     second_weight = 1
#     max_index = 0
#     second_index = 0

#     max_weight_N = 1
#     second_weight_N = 1
#     max_index_N = 0
#     second_index_N = 0

#     for j in range(len(relationships_array)):
#         if(relationships_array[j][1] == 'green'):
#             if relationships_array[j][2] > max_weight:
#                 max_weight = relationships_array[j][2]
#                 max_index = j
#             elif(relationships_array[j][2] > second_weight and relationships_array[j][2] < max_weight):
#                 second_weight = relationships_array[j][2]
#                 second_index = j
#         if(relationships_array[j][1] == 'red'):
#             if relationships_array[j][2] > max_weight_N:
#                 max_weight_N = relationships_array[j][2]
#                 max_index_N = j
#             elif(relationships_array[j][2] > second_weight_N and relationships_array[j][2] < max_weight_N):
#                 second_weight_N = relationships_array[j][2]
#                 second_index_N = j
#     relationships_array[max_index][1] = "orange"
#     relationships_array[second_index][1] = "orange"
#     relationships_array[max_index_N][1] = "orange"
#     relationships_array[second_index_N][1] = "orange"
#     print("正面前二：", relationships_array[max_index], relationships_array[second_index])
#     print("負面前二：", relationships_array[max_index_N], relationships_array[second_index_N])
# return relationships_array
