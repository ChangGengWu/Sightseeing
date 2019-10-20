import pandas as pd
import numpy as np

site_df = pd.read_csv('site_Data.csv')
site_df = site_df.fillna("none")
attr_df = pd.read_csv('site_Attr.csv')

attr_id = attr_df.id.tolist()
attr_c = attr_df.c_Attr.tolist()

site_id = site_df.id.tolist()
site_tag = site_df.tags.tolist()

froM = []
to = []
for i in range(len(site_id)):
    each = site_tag[i].split(" ")
    for j in range(len(each)):
        try:
            # print(site_id[i], each[j], attr_c.index(each[j]))
            froM.append(site_id[i])
            to.append(attr_c.index(each[j])+1)
        except:
            pass
# print(site_tag)

# for k in range(len(froM)):
#     print("form：",froM[k]," to：",to[k])

df = pd.DataFrame({'from': froM, 'to': to})
df.to_csv("site_Relationship.csv", index=False, encoding='utf_8_sig')
