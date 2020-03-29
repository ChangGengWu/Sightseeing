# -*- coding:utf-8 -*-
import difflib
import mysql.connector
cc = "沙雕、便當、玩水、海灘、沙灘、作品、藝術、火車、大眾運輸工具、攜家帶眷、小孩、拍照、戲水、親子、館藏、展品、捷運、交通、咖啡、門票、收費、空調、冷氣、管理、模型、價格、購物、禮品、歌劇院、戲劇院、夕陽、景色、景象、觀景台、環境、標示、登山、停車、車位、太陽、垃圾、垃圾桶、指示、人、公園、土質、樹、溜滑梯、溜冰場、草地、池塘、遊樂區、河堤、遊民、景觀、噴水池、標示、夜景、設備、廁所、寺廟、夜市、美食、廟、攝影、雕塑、遊客、動物、休息、纜車、吃、規劃、購物中心、商店、郊遊、風景、溫泉、態度"
bb = "震撼、精彩、不錯、創意、親民、很棒、好、適合、值得、推薦、美、好玩、喜歡、嘆為觀止、厲害、佩服、好吃、方便、壯觀、開心、欣賞、驚喜、用心、豐富、精緻、優秀、讚嘆、便利、細膩、漂亮、有趣、精美、合理、鬼斧神工、栩栩如生、多、乾淨、齊全、安靜、熱鬧、酷、印象深刻、便宜、美麗、低廉、舒服、種類多、平靜"

good = "不錯 很棒 好 適合 值得 推薦 美 好玩 喜歡 厲害 方便 開心 讚嘆 漂亮 推薦 有趣 多 乾淨 齊全 安靜 熱鬧 酷 印象深刻 美麗 舒服 平靜"

a = "沙雕"
b = "不錯"
c = "沙雕不錯"

if c in b:
    print("good")
else:
    print("nono")

cc_lst = cc.split("、")
bb_lst = bb.split("、")

list_of_tup = [
    (s1, s2) for s1 in cc_lst for s2 in bb_lst if s1 != s2]
# print(list_of_dic)

word_dic = []
for tup in list_of_tup:
    combine = ""
    combine = tup[0] + tup[1]
    #combine_2 = tup[1] + tup[0]
    word_dic.append(combine)
    #word_dic.append(combine_2)
# print(cc_lst)
# print(bb_lst)

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
    print(each[0],"============================================================================")
    result = []
    comment = each[1]
    for i in range(len(comment)):
        end = i + 9
        if i > len(comment):
            compare = comment[i:len(comment)]
            # print(comment[i:len(comment)])
        else:
            compare = comment[i:end]
            # print(comment[i:end])
        for keyword in word_dic:
            seq = difflib.SequenceMatcher(None, keyword, compare)
            ratio = seq.ratio()
            if(ratio >= 0.4):
                result.append([keyword,ratio])
            else:
                continue
    print(result)
    # max = 0
    # second = 0
    # third = 0
    # for m in range(len(result)):
    #     print(result[m][1])
    print("============================================================================")
































# comment = "大坡池為一內陸淡水草澤地，由於天然環境良好，因此動、植物等生態資源十分豐富，各種水生植物與鳥類、蛙類及淡水魚蝦等物種繁多。在台東縣政府的規劃與整治下，目前大坡池水域面積約有20公頃，週邊護岸及濕地也有20公頃左右，設有環湖步道與自行車道，是進行植物觀察、賞鳥、垂釣、健行、騎自行車等休閒活動的理想場所。晴天的清晨很美。"

# keyword = "環境良好"
# result = ""
# max_ratio = 0
# for i in range(len(comment)):
#     end = i + 4
#     if i > len(comment):
#         compare = comment[i:len(comment)]
#         # print(comment[i:len(comment)])
#     else:
#         compare = comment[i:end]
#         # print(comment[i:end])
#     seq = difflib.SequenceMatcher(None, keyword, compare)
#     ratio = seq.ratio()
#     if ratio > max_ratio:
#         max_ratio = ratio
#         result = compare
#     else:
#         continue
# print(result,max_ratio)
