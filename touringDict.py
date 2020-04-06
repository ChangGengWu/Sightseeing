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
                           '擁擠', '不推薦', '簡陋', '老舊', '不好看', '昂貴', '不方便', '不足', '不清楚']
        if self.getClassification() in negative:
            return False
        else:
            return True

    def getClassification(self):
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
