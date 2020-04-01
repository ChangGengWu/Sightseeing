# -*- coding:utf-8 -*-
import difflib
import mysql.connector

#建立connecter
def config():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database='test2',
        buffered=True
    )
    return cnx

#分類


def get_keyword(compare):
    noun = ['Ubike租車站', '大眾運輸工具', 'Ubike', '衛生設備', '保養狀況', '一家大小', '龍舟比賽', '等待時間', '歷史背景', '硬體設備', '遊樂設施', '商城佈置', '購物中心', '全家大小', '攜家帶眷', '親水設施', '美食餐廳', '飲食種類', '自助洗衣', '工作人員', '房間大小', '客房大小', '接待人員', '衛浴空間', '地理位置', '飯店位置', '衛浴設備', 'wifi', 'WIFI', 'Wifi',
            '博物館', '觀景台', '便當店', '棒球場', '戲劇院', '歌劇院', '單車道', '垃圾桶', '哺乳室', '洗手間', '遊戲區', '遊樂區', '溜冰場', '小木屋', '櫻花樹', '噴水池', '手扶梯', '動物園', '戲水區', '停車場', '選擇性', '美食街', '腳踏車', '自行車', '溜滑梯', '停車位', 'cp值', '性價比', '按摩椅', '房務員', '洗衣機', '吃東西', '行李員', '清潔度', '蓮蓬頭', '小朋友', 'CP值', '出水量', 'Cp值', '建築', '整修', '門票', '態度', '交通', '遮避', '燈塔', '風車', '人潮', '台鐵', '高鐵', '座位', '規模', '溫泉', '纜車', '沙雕', '寺廟', '路燈', '座椅', '冷氣', '空調', '氣味', '垃圾', '山路', '空氣', '登山', '綠地', '陰影', '河堤', '土質', '池塘', '草地', '風景', '夜景', '景觀', '太陽', '環境', '景象', '景色', '品牌', '電梯', '裝飾', '商店', '禮品', '購物', '價格', '收費', '動線', '服務', '標示', '指示', '規劃', '管理', '遊客', '遊民', '親子', '小孩', '野餐', '郊遊', '休息', '攝影', '拍照', '動物', '海邊', '海岸', '戲水', '沙灘', '海灘', '作品', '玩水', '雕塑', '模型', '展品', '館藏', '藝術', '會車', '動向', '路線', '車位', '停車', '捷運', '火車', '餐點', '夜市', '美食', '咖啡', '便當', '晚餐', '午餐', '人員', '小吃', '廁所', '公園', '湖景', '夕陽', '逛街', '步道', '空間', '房間', '餐廳', '窗戶', '設備', '清潔', '車站', '職員', '員工', '設計', '價錢', '光線', '照明', '熱水', '位置', '飲料', '浴室', '水壓', '品質', '浴缸', '尺寸', '食物', '地點', '設施', '隔音', '市景', '早餐', '用餐', '衛浴', '洗衣', '茶水', '周邊', '商圈', '床單', '枕頭', '被單', '房型', '格局', '機場', '灰塵', '異味', '前台', '飯店', '地毯', '地板', '帶位', '裝修', '價位', '床鋪', '採光', '硬體', '效率', '插座', '氣氛', '電視', '走道', '坪數', '入園', '廟', '人', '床']


    adj = ['不是特別好', '一位難求', '不太足夠', '非常不好', '不夠清楚', '不夠簡單', '非常難找', '印象深刻', '嘆為觀止', '路途遙遠', '相當不便', '栩栩如生', '鬼斧神工', '沒有很多', '不太穩定', '愛理不理', '態度很差', '美中不足', '不具備', '沒禮貌', '有耐心', '有禮貌', '再加強', '不理想', '不建議', '沒品質', '不值得', '最棒的', '特別好', '差太多', '不清楚', '更舒服', '沒耐性', '不方便', '超方便', '不乾淨', '不好吃', '種類多', '美麗的', '漂亮的', '蠻貴的', '不便宜', '不用錢', '很實惠', '有點小', '蠻小的', '蠻大的', '有點少', '非常少',
           '有點多', '多到爆', '非常多', '不穩定', '不耐煩', '不足夠', '不夠冷', '不齊全', '足夠的', '態度差', '態度好', '不和善', '沒耐心', '有落差','沒有','具備', '用心', '和善', '不便', '不易', '詭異', '害怕', '危險', '掃興', '差勁', '不推', '糟糕', '良好', '齊全', '推薦', '開心', '喜歡', '好玩', '推薦', '適合', '值得', '複雜', '失望', '新鮮', '明亮', '寬敞', '優美', '舒服', '舒適', '熱鬧', '平靜', '擁擠', '讚嘆', '佩服', '厲害', '震撼', '壯觀', '遙遠', '傲慢', '塞車', '蠻多', '超多', '很多', '許多', '不佳', '不全', '不良', '不遠', '不近', '不多', '不少', '誠懇', '豪華', '穩定', '周到', '漂亮', '美麗', '細心', '豐盛', '親切', '方便', '專業', '熱心', '新穎', '一般', '適中', '鄰近', '完善', '老舊', '迅速', '異常',
       '雅緻', '冷淡', '有力', '簡陋', '滿滿', '大量', '不高', '不低', '實惠', '平價', '低廉', '合理', '親民', '免費', '蠻貴', '超貴', '很貴', '好美', '難看', '難吃', '精美', '精緻', '無聊', '無趣', '細膩', '優秀', '驚喜', '很棒', '創意', '強大', '不錯', '有趣', '整潔', '乾淨', '骯髒', '便利', '不夠', '不足', '足夠', '難求', '紊亂', '寧靜', '安靜', '慢', '久', '低', '醜', '爛', '酷', '擠', '兇', '髒', '亂', '凍', '寒', '冷', '熱', '曬', '醜', '美', '貴', '小', '大', '少', '多', '遠', '近', '佳', '棒', '軟', '有', '優', '高', '怪', '貴', '悶', '夠']
    result_noun = ""
    result_adj = ""
    for n in noun:
        if n in compare:
            result_noun = n
            break
        else:
            continue
    compare.replace(result_noun, "")
    for a in adj:
        if a in compare:
            result_adj = a
            break
        else:
            continue
    keyword = ""
    if(result_noun == "" or result_adj == ""):
        pass
    else:
        print(compare)
        classified = classified_adj(result_adj)
        keyword = result_noun + classified
    return keyword


def classified_adj(adjs):
    many = ['種類多', '有點多', '多到爆', '非常多', '蠻多', '超多',
            '很多', '許多', '滿滿', '不少', '多', '大量', '豐富', '多']
    few = ['沒有很多', '有點少', '非常少', '超少', '蠻少', '很少', '較少', '不多', '少']
    big = ['蠻大的', '巨大', '超大', '很大', '大', '寬敞']
    small = ['有點小', '蠻小的', '蠻小', '很小', '窄小', '小']
    high = ['高', '不低']
    low = ['低', '不高']
    inexpensive = ['很實惠', '便宜', '實惠', '平價', '低廉', '合理', '親民']
    free = ['不用錢', '免費']
    expensive = ['蠻貴的', '不便宜', '蠻貴', '超貴', '很貴', '貴']
    beautiful = ['美麗的', '漂亮的', '好美', '美', '精緻',
             '栩栩如生', '鬼斧神工', '精美', '壯觀', '雅緻', '漂亮', '美麗']
    ugly = ['難看', '醜']
    delicious = ['好吃']
    yucky = ['不好吃', '難吃']
    wonderful = ['厲害', '細膩', '用心', '驚喜', '很棒', '創意', '強大']
    boring = ['無聊', '無趣']
    interesting = ['有趣']
    hot = ['不夠冷', '熱', '曬', '悶']
    cold = ['凍', '寒', '冷']
    clean = ['整潔', '乾淨']
    mess = ['不乾淨', '骯髒', '亂', '髒']
    convenient = ['超方便', '便利', '方便']
    inconvenient = ['相當不便', '不方便', '不便', '塞車']
    insufficient = ['不太足夠', '不足夠', '不夠', '不足', '不齊全', '不全']
    sufficient = ['齊全', '足夠的', '足夠', '夠']
    good_manner = ['有耐心', '有禮貌', '態度好', '和善',
               '用心', '親切', '友善', '熱心', '專業', '細心', '周到', '誠懇']
    bad_manner = ['態度很差', '態度差', '沒禮貌', '不和善',
              '沒耐心', '沒耐性', '傲慢', '兇', '愛理不理', '不耐煩', '冷淡']
    far = ['路途遙遠', '遙遠', '遠', '不近']
    close = ['鄰近', '近', '不遠']
    recommend = ['印象深刻', '嘆為觀止', '讚嘆', '佩服', '震撼', '特別好', '沒話說',
             '推薦', '開心', '喜歡', '好玩', '適合', '值得', '酷', '常來', '不錯']
    hard_to_find = ['非常難找', '難求', '一位難求']
    many_people = ['擁擠', '紊亂', '擠']
    quient = ['寧靜', '安靜', '平靜']
    lively = ['熱鬧']
    comfortable = ['更舒服', '舒適', '新鮮', '明亮', '優美', '舒服']
    blurry = ['不夠清楚', '不夠簡單', '有落差', '差太多', '不清楚', '複雜', '失望', '不易']
    good = ['最棒的', '特別好', '沒話說', '良好', '優秀', '好', '棒', '好', '優', '佳']
    bad = ['不是特別好', '非常不好', '美中不足', '再加強', '不理想', '不建議', '沒品質', '不值得',
       '詭異', '害怕', '危險', '掃興', '差勁', '不推', '糟糕', '爛', '不良', '不佳']
    have = ['有', '具備']
    no_have = ['沒有', '不具備']
    not_stable = ['不太穩定', '不穩定']
    stable = ['穩定']
    elses = ['簡陋', '有力', '異常', '迅速', '老舊', '完善',
         '適中', '一般', '新穎', '豐盛', '豪華', '怪', '軟', '久', '慢']
    conclusion = ""
    if(adjs in many):
        conclusion = "多"
    elif(adjs in few):
        conclusion = "少"
    elif(adjs in big):
        conclusion = "大"
    elif(adjs in small):
        conclusion = "小"
    elif(adjs in inexpensive):
        conclusion = "便宜"
    elif(adjs in free):
        conclusion = "免費"
    elif(adjs in expensive):
        conclusion = "昂貴"
    elif(adjs in beautiful):
        conclusion = "美麗"
    elif(adjs in ugly):
        conclusion = "不好看"
    elif(adjs in delicious):
        conclusion = "好吃"
    elif(adjs in yucky):
        conclusion = "難吃"
    elif(adjs in wonderful):
        conclusion = "值得一看"
    elif(adjs in boring):
        conclusion = "無趣"
    elif(adjs in hot):
        conclusion = "炎熱"
    elif(adjs in cold):
        conclusion = "寒冷"
    elif(adjs in clean):
        conclusion = "乾淨"
    elif(adjs in mess):
        conclusion = "髒亂"
    elif(adjs in convenient):
        conclusion = "方便"
    elif(adjs in inconvenient):
        conclusion = "不方便"
    elif(adjs in insufficient):
        conclusion = "不足"
    elif(adjs in good_manner):
        conclusion = "態度優良"
    elif(adjs in bad_manner):
        conclusion = "態度不佳"
    elif(adjs in far):
        conclusion = "遙遠"
    elif(adjs in recommend):
        conclusion = "推薦前往"
    elif(adjs in hard_to_find):
        conclusion = "難找"
    elif(adjs in many_people):
        conclusion = "擁擠"
    elif(adjs in quient):
        conclusion = "寧靜"
    elif(adjs in lively):
        conclusion = "熱鬧"
    elif(adjs in comfortable):
        conclusion = "舒適"
    elif(adjs in blurry):
        conclusion = "不清楚"
    elif(adjs in good):
        conclusion = "評價好的"
    elif(adjs in bad):
        conclusion = "不推薦"
    elif (adjs in elses):
         conclusion = adjs
    elif (adjs in close):
        conclusion = "鄰近"
    elif (adjs in sufficient):
         conclusion = "齊全"
    elif (adjs in high):
         conclusion = "高"
    elif (adjs in low):
         conclusion = "低"
    elif (adjs in interesting):
          conclusion = "有趣"
    elif (adjs in have):
          conclusion = "具備"
    elif (adjs in no_have):
          conclusion = "不具備"
    elif (adjs in stable):
          conclusion = "穩定"
    elif (adjs in not_stable):
          conclusion = "不穩定"
    return conclusion

def comment_seg(cnx):
    cursor_all = cnx.cursor()
    sql = "SELECT id,comment,evaluation,site_ID FROM `user_comment3` WHERE site_ID = 'S0102'"
    cursor_all.execute(sql)
    for each in cursor_all:
        result = []
        comment = each[1]
        evaluation = each[2]
        site_id = each[3]
        color = eval_to_color(evaluation)
        print("=================================================")
        print(comment)
        keyword_lst = []
        strip_chars = '？"。.，,！～!~《》[]〖〗“”  )('
        comment = comment.translate(
            comment.maketrans(dict.fromkeys(strip_chars, "#")))
        seg_lst = comment.split("#")
        for seg in seg_lst:
            keyword = get_keyword(seg)
            print(keyword)
        #     if(keyword != "" and keyword not in keyword_lst):
        #         keyword_lst.append(keyword)
        # for word in keyword_lst:
        #     shape = "circle"
        #     idid = ""
        #     add_Data(cnx, idid, word, color, shape, site_id)
        # build_relationship(cnx, keyword_lst, color, site_id)


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


def add_Relationship(cnx,from_id, to_id, site_id):
    cursor = cnx.cursor()
    add_relation = ("INSERT INTO `segment_relationship`"
                    "(from_id, to_id, site_id) "
                    "VALUES (%s,%s,%s)")
    data = (from_id, to_id, site_id)
    cursor.execute(add_relation, data)
    cnx.commit()


def eval_to_color(eval):
    color = "green"
    if(eval == "正面評價"):
        color = color
    else:
        color = "red"
    return color


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
