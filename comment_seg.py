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
    #array that save node's value,color,weight
    nodes_array = [["value", "color", "weight"]]
    #array that save relationships's from,to,weight
    relationships_array = [[["from", "color"], ["to", "color"], "weight"]]
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
                if (color == "green") and (concludsion not in positive_seg):
                    positive_seg.append(concludsion)
                elif (color == "red") and (concludsion not in negative_seg):
                    negative_seg.append(concludsion)
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
                print(each[0][0], from_seg)
                #如果from to 值相同且顏色同為綠色 weight+1

                #unfinish
                if(each[0] == from_seg and each[1] == to_seg and each[0][1] == "green" and each[1][1] == "green") or (each[1] == from_seg and each[0] == to_seg and each[0][1] == "green" and each[1][1] == "green"):
                    print(each[0], each[1], each[2])
                    each[2] += 1
                    flag = 1
                else:
                    print("nononononnon")
            if flag == 0:
                relationships_array.append(
                    [[from_seg, "green"], [to_seg, "green"], 1])
        
        for i in range(len(negative_seg) - 1):
            from_seg = negative_seg[i]
            to_seg = negative_seg[i+1]
            flag = 0
            for each in relationships_array:
                #如果from to 值相同且顏色同為綠色 weight+1
                print(each[0][0],from_seg)
                if(each[0][0] == from_seg and each[1][0] == to_seg and each[0][1] == "red" and each[1][1] == "red") or (each[1][0] == from_seg and each[0][0] == to_seg and each[0][1] == "red" and each[1][1] == "red"):
                    each[2] += 1
                    flag = 1
                else:
                    print("nononononnon")
            if flag == 0:
                relationships_array.append(
                    [[from_seg, "red"], [to_seg, "red"], 1])

    # for node in nodes_array:
    #     print(node)
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


#add segment to database
def add_Data(cnx,new_id, segment, color, shape, site_id):
    cursor = cnx.cursor(buffered=True)
    if_exist = check_exist(cnx,segment, color, site_id)
    if (if_exist == True):
        pass
    else:
        add_data = ("INSERT INTO segment_data"
                    "(id, segment, color, shape, site_id)"
                    "VALUES (%s,%s,%s,%s,%s)")
        data = (new_id, segment, color, shape, site_id)
        cursor.execute(add_data, data)
        cnx.commit()

#check if segment exist in database
def check_exist(cnx,segment, color, site_id):
    cursor = cnx.cursor(buffered=True)
    sql = "SELECT id FROM segment_data WHERE segment = '" + segment + \
        "' AND color = '" + color + "' AND site_id = '" + site_id + "'"
    cursor.execute(sql)
    entry = cursor.fetchone()
    if entry is None:
        return False
    else:
        return True

#add relationship to database
def add_Relationship(cnx,from_id, to_id, site_id):
    cursor = cnx.cursor()
    add_relation = ("INSERT INTO `segment_relationship`"
                    "(from_id, to_id, site_id) "
                    "VALUES (%s,%s,%s)")
    data = (from_id, to_id, site_id)
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

#bulid relationship (red to red) (green to green) in each comment
def build_relationship(cnx,keyword_lst, color, site_id):
    for i in range(len(keyword_lst) - 1):
        print(keyword_lst[i], color)
        cursor1 = cnx.cursor(buffered=True)
        cursor2 = cnx.cursor(buffered=True)
        sql = "SELECT id FROM `segment_data` WHERE segment = '" + \
            keyword_lst[i] + "' AND color = '" + color + "'"
        sql_2 = "SELECT id FROM `segment_data` WHERE segment = '" + \
            keyword_lst[i+1] + "' AND color = '" + color + "'"
        cursor1.execute(sql)
        cursor2.execute(sql_2)
        from_id = ""
        to_id = ""
        for ele in cursor1:
            from_id = ele[0]
        for elee in cursor2:
            to_id = elee[0]
        add_Relationship(cnx,from_id, to_id, site_id)

def main():
    cnx = config()
    comment_seg(cnx)

main()
