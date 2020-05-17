# -*- coding:utf-8 -*-


class touringDict:
    sentence = " "
    result_noun = ""
    result_adj = " "

    def __init__(self, string=""):
        self.sentence = string

    # noun = getNoun(sentence)
    # adj = getAdj(sentence)
    # conclusion = noun + adj

    #sentence setter
    def setSentence(self,new_sentence):
        self.sentence = new_sentence

    #conclusion getter
    def getConclusion(self):
        n = self.getNoun()
        adj = self.getAdj()
        classification = self.getClassification()
        conclusion = str(n) + str(classification)
        print(conclusion)
        conclude = dictFilter(conclusion)
        return conclude
        
    #noun getter
    def getNoun(self):
        noun = []
        with open('tourNoun.txt', 'r', encoding='UTF-8', errors='ignore') as file:
            for data in file.readlines():
                data = data.strip()
                noun.append(data)
        for n in noun:
            if n in self.sentence:
                result_noun = n
                break
            else:
                result_noun = None
        return result_noun

    #adj getter
    def getAdj(self):
        adj = []
        with open('tourAdj.txt', 'r', encoding='UTF-8', errors='ignore') as file:
            for data in file.readlines():
                data = data.strip()
                adj.append(data)
        for a in adj:
            if a in self.sentence:
                result_adj = a
                break
            else:
                result_adj = None
        return result_adj
    
    #return positive or negative
    def ifPositive(self):
        negative = ['髒亂', '難吃', '無趣', '態度不佳', '難找',
                    '擁擠', '評價差的', '簡陋', '老舊', '不好看', '昂貴', '不方便', '不足', '不清楚', '不具備']
        positive = ['便宜', '免費', '美麗', '好吃', '值得一看',
                    '乾淨', '方便', '態度優良', '推薦前往', '舒適', '評價好的', '齊全', '有趣', '完善', '新穎', '豐盛', '豪華']
        if self.getClassification() in negative:
            return 0
        if self.getClassification() in positive:
            return 1
        else:
            return 2
    def getClassification(self):
        human = ["人", "小孩", "老人", "小朋友", "老年人", "身障者",
                 "年長者", "年長的人", "遊客", "親子", "遊民", "一家大小"]
        noun = self.getNoun()
        adjs = self.getAdj()
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
        delicious = ['好吃',"美味",'美食']
        yucky = ['不好吃', '難吃']
        wonderful = ['厲害', '細膩', '用心', '驚喜', '很棒', '強大']
        boring = ['無聊', '無趣']
        interesting = ['有趣', '好玩', '開心']
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
        recommend = ['推薦', '喜歡', '適合', '值得']
        hard_to_find = ['非常難找', '難求', '一位難求']
        many_people = ['擁擠', '紊亂', '擠']
        quient = ['寧靜', '安靜', '平靜']
        lively = ['熱鬧']
        comfortable = ['更舒服', '舒適', '新鮮', '明亮', '優美', '舒服']
        blurry = ['不夠清楚', '不夠簡單', '有落差', '不清楚', '複雜', '不易']
        good = ['最棒的', '特別好', '沒話說', '良好', '優秀',
                '好', '棒', '好', '優', '佳', '沒話說', '不錯', '印象深刻', '嘆為觀止', '讚嘆', '震撼']
        bad = ['不是特別好', '非常不好', '美中不足', '再加強', '不理想', '不建議', '沒品質', '不值得',
               '詭異', '害怕', '危險', '掃興', '差勁', '不推', '糟糕', '爛', '不良', '不佳', '失望', '不適合', '不是很好']
        have = ['有', '具備']
        no_have = ['沒有', '不具備', '沒']
        not_stable = ['不太穩定', '不穩定']
        stable = ['穩定']
        elses = ['簡陋', '有力', '異常', '迅速', '老舊', '完善',
                 '適中', '一般', '新穎', '豐盛', '豪華', '怪', '軟', '久', '慢', '硬']
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
            if noun in human:
                conclusion = "覺得便宜"
            else:
                conclusion = "便宜"
        elif(adjs in free):
            conclusion = "免費"
        elif(adjs in expensive):
            if noun in human:
                conclusion = "覺得昂貴"
            else:
                conclusion = "昂貴"
        elif(adjs in beautiful):
            if noun in human:
                conclusion = "覺得美麗"
            else:
                conclusion = "美麗"
        elif(adjs in ugly):
            if noun in human:
                conclusion = "覺得不好看"
            else:
                conclusion = "不好看"
        elif(adjs in delicious):
            if noun in human:
                conclusion = "覺得好吃"
            else:
                conclusion = "好吃"
        elif(adjs in yucky):
            if noun in human:
                conclusion = "覺得難吃"
            else:
                conclusion = "難吃"
        elif(adjs in wonderful):
            conclusion = "值得一看"
        elif(adjs in boring):
            if noun in human:
                conclusion = "覺得無趣"
            else:
                conclusion = "無趣"
        # elif(adjs in hot):
        #     if noun in human:
        #         conclusion = "覺得炎熱"
        #     else:
        #         conclusion = "炎熱"
        # elif(adjs in cold):
        #     if noun in human:
        #         conclusion = "覺得寒冷"
        #     else:
        #         conclusion = "寒冷"
        elif(adjs in clean):
            if noun in human:
                conclusion = "覺得乾淨"
            else:
                conclusion = "乾淨"
        elif(adjs in mess):
            if noun in human:
                conclusion = "覺得髒亂"
            else:
                conclusion = "髒亂"
        elif(adjs in convenient):
            if noun in human:
                conclusion = "覺得方便"
            else:
                conclusion = "方便"
        elif(adjs in inconvenient):
            if noun in human:
                conclusion = "覺得不方便"
            else:
                conclusion = "不方便"
        elif(adjs in insufficient):
            conclusion = "不足"
        elif(adjs in good_manner):
            conclusion = "態度優良"
        elif(adjs in bad_manner):
            conclusion = "態度不佳"
        elif(adjs in far):
            if noun in human:
                conclusion = "覺得遙遠"
            else:
                conclusion = "遙遠"
        elif(adjs in recommend):
            conclusion = "推薦前往"
        elif(adjs in hard_to_find):
            if noun in human:
                conclusion = "覺得難找"
            else:
                conclusion = "難找"
        elif(adjs in many_people):
            if noun in human:
                conclusion = "覺得擁擠"
            else:
                conclusion = "擁擠"
        elif(adjs in quient):
            if noun in human:
                conclusion = "覺得寧靜"
            else:
                conclusion = "寧靜"
        elif(adjs in lively):
            if noun in human:
                conclusion = "覺得熱鬧"
            else:
                conclusion = "熱鬧"
        elif(adjs in comfortable):
            if noun in human:
                conclusion = "覺得舒適"
            else:
                conclusion = "舒適"
        elif(adjs in blurry):
                conclusion = "不清楚"
        elif(adjs in good):
            if noun in human:
                conclusion = "覺得評價好的"
            else:
                conclusion = "評價好的"
        elif(adjs in bad):
            if noun in human:
                conclusion = "覺得評價差的"
            else:
                conclusion = "評價差的"
        elif (adjs in elses):
            if noun in human:
                conclusion = "覺得" + adjs
            else:
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
            if noun in human:
                conclusion = "覺得有趣"
            else:
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

def dictFilter(conclusion):
    filter_dict = []
    with open('dict.txt', 'r', encoding='UTF-8', errors='ignore') as file:
        for data in file.readlines():
            data = data.strip()
            filter_dict.append(data)
    if conclusion in filter_dict:
        return conclusion
    else:
        return None
