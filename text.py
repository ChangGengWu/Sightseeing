import mysql.connector
import re
print("=============start=============", end='\n')

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test1'
)
cursor = cnx.cursor(buffered=True)
query1 = "SELECT id,name FROM site"
cursor.execute(query1)
for each in cursor:
    id = each[0]
    name = each[1].split(" ")
    print(id + " " + name[0])
    cursor2 = cnx.cursor(buffered=True)
    query2 = ("UPDATE site"
         " SET name=%s"
         " WHERE id=%s")
    data = (name[0],id)
    cursor2.execute(query2,data)
    cnx.commit()
# for each in cursor:
#     a = each[0].split(" ")
#     print(a[0])


# target = [["基隆", "https://www.tripadvisor.com.tw/Attractions-g317130-Activities-Keelung.html"],
#           ["台北", "https://www.tripadvisor.com.tw/Attractions-g293913-Activities-Taipei.html"],
#           ["新北", "https://www.tripadvisor.com.tw/Attractions-g1432365-Activities-New_Taipei.html"],
#           ["桃園", "https://www.tripadvisor.com.tw/Attractions-g297912-Activities-Taoyuan.html"],
#           ["新竹", "https://www.tripadvisor.com.tw/Attractions-g297906-Activities-Hsinchu.html"],
#           ["苗栗", "https://www.tripadvisor.com.tw/Attractions-g616038-Activities-Miaoli.html"],
#           ["台中", "https://www.tripadvisor.com.tw/Attractions-g297910-Activities-Taichung.html"],
#           ["彰化", "https://www.tripadvisor.com.tw/Attractions-g304153-Activities-Changhua.html"],
#           ["雲林", "https://www.tripadvisor.com.tw/Attractions-g616037-Activities-Yunlin.html"],
#           ["嘉義", "https://www.tripadvisor.com.tw/Attractions-g1433864-Activities-Chiayi_County.html"],
#           ["嘉義", "https://www.tripadvisor.com.tw/Attractions-g297904-Activities-Chiayi.html"],
#           ["高雄", "https://www.tripadvisor.com.tw/Attractions-g297908-Activities-Kaohsiung.html"],
#           ["屏東", "https://www.tripadvisor.com.tw/Attractions-g297909-Activities-Pingtung.html"],
#           ["台東", "https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung.html"],
#           ["花蓮", "https://www.tripadvisor.com.tw/Attractions-g297907-Activities-Hualien.html"],
#           ["宜蘭", "https://www.tripadvisor.com.tw/Attractions-g608526-Activities-Yilan.html"],
#           ["澎湖", "https://www.tripadvisor.com.tw/Attractions-g1437280-Activities-Penghu.html"],
#           ["金門", "https://www.tripadvisor.com.tw/Attractions-g1152699-Activities-Kinmen.html"],
#           ["馬祖", "https://www.tripadvisor.com.tw/Attractions-g1731586-Activities-Matsu.html"]]
