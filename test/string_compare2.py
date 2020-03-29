# -*- coding:utf-8 -*-
import difflib
import mysql.connector

#分類
def get_keyword(compare):
    noun = ['吃','人','廟', '便當', '咖啡', '美食', '夜市', '餐點', '火車', '捷運', '停車', '車位', '路線', '動向', '會車', '藝術', '館藏', '展品', '模型', '雕塑',
            '玩水', '海灘', '沙灘', '戲水', '海岸', '海邊', '動物', '拍照', '攝影', '休息', '郊遊', '野餐', '小孩', '親子', '遊民', '遊客', '管理', '規劃', '指示', '標示', '服務', '動線', '收費', '價格', '購物', '禮品', '商店', '裝飾', '電梯', '品牌', '景色', '景象', '環境', '太陽', '景觀', '夜景', '風景', '草地', '池塘', '土質', '河堤', '陰影', '綠地', '登山', '空氣', '山路', '垃圾', '氣味', '空調', '冷氣', '座椅', '路燈', '寺廟', '沙雕', '纜車', '溫泉', '規模', '風車', '燈塔', '美食街', '選擇性', '停車場', '戲水區', '動物園', '手扶梯', '噴水池', '櫻花樹', '小木屋', '溜冰場', '遊樂區', '遊戲區', '洗手間', '哺乳室', '垃圾桶', '單車道', '歌劇院', '戲劇院', '棒球場', '便當店', '餐廳選擇', '飲食種類', '美食餐廳', '小吃交通', '親水設施', '攜家帶眷', '全家大小', '整修門票', '購物中心', '商城佈置', '逛街夕陽', '湖景公園', '遊樂設施', '硬體設備', '歷史背景', '等待時間', '龍舟比賽', '食品選擇性', '停車位作品', '遮避觀景台', '步道溜滑梯', '停車場氣味', '大眾運輸工具', '一家大小態度', '保養狀況廁所', '環境衛生設備']

    adj = ['多', '少', '大', '小', '貴', '美', '醜', '曬', '熱', '冷', '寒', '凍', '亂', '髒', '兇', '擠', '酷', '爛', '醜', '低', '久', '慢', '許多', '很多', '超多', '蠻多', '較少', '很少', '蠻少', '超少', '很大', '超大', '巨大', '窄小', '很小', '蠻小', '親民', '合理', '低廉', '平價', '實惠', '便宜', '免費', '很貴', '超貴', '蠻貴', '好美', '難看', '好吃', '精緻', '難吃', '不錯', '創意', '很棒', '驚喜', '用心', '豐富', '優秀', '細膩', '有趣', '厲害', '精美', '無趣', '無聊', '乾淨', '整潔', '骯髒', '便利', '不錯', '塞車', '傲慢', '遙遠', '壯觀', '震撼', '厲害', '佩服', '讚嘆', '車多', '擁擠', '平靜', '熱鬧', '舒適', '舒服', '優美', '寬敞', '明亮', '新鮮', '不易', '錯誤', '失望', '複雜', '值得', '適合', '推薦', '好玩', '喜歡', '開心', '推薦', '齊全', '良好', '糟糕', '不推', '差勁', '掃興', '危險', '害怕', '詭異', '不易', '不便', '和善', '非常多', '多到爆', '有點多', '非常少', '有點少', '蠻大的', '小點小', '蠻小的', '有點小', '很實惠', '不用錢', '不便宜', '蠻貴的', '漂亮的', '美麗的', '種類多', '不好吃', '不乾淨', '超方便', '不方便', '沒耐性', '更舒服', '不清楚', '差太多', '特別好', '最棒的', '不值得', '沒品質', '不建議', '不理想', '再加強', '態度好', '有禮貌', '有耐心', '沒禮貌', '態度差', '沒有很多', '印象深刻', '鬼斧神工', '栩栩如生', '印象深刻', '相當不便', '路途遙遠', '嘆為觀止', '鬼斧神工', '印象深刻', '鬼斧神工', '非常難找', '不夠簡單', '不夠清楚', '非常不好', '態度很好', '態度很差','一位難求''不是特別好', '不太足夠用心']
    result_noun = ""
    result_adj = ""
    for n in noun:
        if n in compare:
            result_noun = n
        else:
            continue
    for a in adj:
        if a in compare:
            result_adj = a
        else:
            continue
    keyword = ""
    if(result_noun == "" or result_adj == ""):
        pass
    else:
        classified = classified_adj(result_adj)
        keyword = result_noun + classified
    return keyword

def classified_adj(adj):
    many = ['種類多', '有點多', '多到爆', '非常多', '蠻多', '超多', '很多', '許多', '多']
    few = ['沒有很多', '有點少', '非常少', '超少', '蠻少', '很少', '較少', '少']
    big = ['小點小', '蠻大的', '巨大', '超大', '很大', '大']
    small = ['有點小', '蠻小的', '蠻小', '很小', '窄小', '小']
    inexpensive = ['很實惠', '便宜', '實惠', '平價', '低廉', '合理', '親民']
    free = ['不用錢', '免費']
    expensive = ['蠻貴的', '不便宜', '蠻貴', '超貴', '很貴', '貴']
    beautiful = ['美麗的', '漂亮的', '好美', '美']
    ugly = ['難看', '醜']
    delicious = ['好吃']
    yucky = ['不好吃', '難吃']
    wonderful = ['印象深刻', '栩栩如生', '鬼斧神工', '印象深刻', '精美', '精緻', '厲害',
             '有趣', '細膩', '優秀', '豐富', '用心', '驚喜', '很棒', '創意', '不錯']
    boring = ['無聊', '無趣']
    hot = ['熱', '曬']
    cold = ['凍', '寒', '冷']
    clean = ['整潔', '乾淨']
    mess = ['不乾淨', '骯髒', '亂']
    convenient = ['超方便', '不錯', '便利']
    inconvenient = ['相當不便', '不方便', '不便', '塞車']
    insufficient = ['不太足夠', '不足夠', '不夠', '不足']
    good_manner = ['態度很好', '有耐心', '有禮貌', '態度好', '和善', '用心']
    bad_manner = ['態度很差', '態度差', '沒禮貌', '不和善', '沒耐心', '沒耐性', '傲慢', '兇']
    far = ['路途遙遠', '遙遠', '遠']
    recommend = ['鬼斧神工', '印象深刻', '鬼斧神工', '嘆為觀止', '讚嘆', '佩服', '厲害', '震撼', '壯觀']
    hard_to_find = ['非常難找', '車多', '難求','一位難求']
    many_people = ['人潮多', '擁擠', '擠']
    quient = ['寧靜', '安靜', '平靜']
    lively = ['熱鬧']
    comfortable = ['更舒服', '舒適', '新鮮', '明亮', '寬敞', '優美', '舒服']
    blurry = ['不夠清楚', '不夠簡單', '有落差', '差太多', '不清楚', '複雜', '失望', '錯誤', '不易']
    good = ['最棒的', '特別好', '沒話說', '良好', '齊全', '有趣', '推薦',
        '開心', '喜歡', '好玩', '推薦', '適合', '值得', '酷']
    bad = ['不是特別好', '非常不好', '再加強', '不理想', '不建議', '沒品質', '不值得', '不易',
       '詭異', '害怕', '危險', '掃興', '差勁', '不推', '糟糕', '低', '醜', '爛']
    conclusion = ""
    if(adj in many):
        conclusion = "多的"
    elif(adj in few):
        conclusion = "少的"
    elif(adj in big):
        conclusion = "大的"
    elif(adj in small):
        conclusion = "小的"
    elif(adj in inconvenient):
        conclusion = "便宜的"
    elif(adj in free):
        conclusion = "免費的"
    elif(adj in expensive):
        conclusion = "昂貴的"
    elif(adj in beautiful):
        conclusion = "美麗的"
    elif(adj in ugly):
        conclusion = "不好看的"
    elif(adj in delicious):
        conclusion = "好吃的"
    elif(adj in yucky):
        conclusion = "難吃的"
    elif(adj in wonderful):
        conclusion = "精彩壯麗的"
    elif(adj in boring):
        conclusion = "無趣的"
    elif(adj in hot):
        conclusion = "炎熱的"
    elif(adj in cold):
        conclusion = "寒冷的"
    elif(adj in clean):
        conclusion = "乾淨的"
    elif(adj in mess):
        conclusion = "髒亂的"
    elif(adj in convenient):
        conclusion = "方便的"
    elif(adj in inconvenient):
        conclusion = "不方便的"
    elif(adj in insufficient):
        conclusion = "不足的"
    elif(adj in good_manner):
        conclusion = "服務優良的"
    elif(adj in bad_manner):
        conclusion = "服務不佳的"
    elif(adj in far):
        conclusion = "遙遠的"
    elif(adj in recommend):
        conclusion = "推薦的"
    elif(adj in hard_to_find):
        conclusion = "難找的"
    elif(adj in many_people):
        conclusion = "擁擠的"
    elif(adj in quient):
        conclusion = "寧靜的"
    elif(adj in lively):
        conclusion = "熱鬧的"
    elif(adj in comfortable):
        conclusion = "舒適的"
    elif(adj in blurry):
        conclusion = "不清楚的"
    elif(adj in good):
        conclusion = "評價好的"
    elif(adj in bad):
        conclusion = "評價差的"
    else:
        conclusion = "好評的"
    return conclusion

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test1'
)
cursor = cnx.cursor()
sql = "SELECT id,comment FROM `user_comment3` WHERE site_ID = 'S0099'"
cursor.execute(sql)

for each in cursor:
    result = []
    comment = each[1]
    print("=================================================")
    print(comment)
    keyword_lst = []
    for i in range(len(comment)):
        end = i + 10
        if end > len(comment):
            pass
        else:
            compare = comment[i:end]
            # print(comment[i:end])
        keyword = get_keyword(compare)
        if(keyword != "" and keyword not in keyword_lst):
            keyword_lst.append(keyword)
    print(keyword_lst)
