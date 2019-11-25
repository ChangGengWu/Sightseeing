#install.packages("DBI")
#install.packages("odbc")
install.packages("RMySQL")
library("RMySQL");
#連結資料庫
con = dbConnect(MySQL(), user = 'root', password = '12345678', dbname = 'test1',
                            host = 'localhost')
#轉碼(讓中文顯示)
dbSendQuery(con,"SET NAMES big5")
#query
result = dbSendQuery(con, "select * from test WHERE id=4")
#執行query
data.frame = fetch(result)
x <- data.frame
x$string
nodes <- data.frame(id = c(x$id),label = c(x$string))
visNetwork(nodes,idth = "100%",height = "500px")%>%
  visEdges(smooth = FALSE)