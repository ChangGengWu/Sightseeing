#install.packages("DBI")
#install.packages("odbc")
library("RMySQL");
library("visNetwork");
#連結資料庫
con = dbConnect(MySQL(), user = 'root', password = '12345678', dbname = 'test1',
                            host = 'localhost')
#轉碼(讓中文顯示)
dbSendQuery(con,"SET NAMES big5")
#query
result = dbSendQuery(con, "SELECT * FROM site WHERE id BETWEEN 'S0002' AND 'S0080'")
#執行query
data.frame = fetch(result)
x <- data.frame

nodes <- data.frame(id = c(x$id),label = c(x$name), shape='circle')
visNetwork(nodes,width = "100%",height = "500px")%>%
  visEdges(smooth = FALSE)