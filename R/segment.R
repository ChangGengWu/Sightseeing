library("RMySQL");
library("visNetwork");
library('igraph')
con = dbConnect(MySQL(), user = 'root', password = '12345678', dbname = 'test1',
                host = 'localhost')
dbSendQuery(con,"SET NAMES big5")

segment <- dbGetQuery(con, "SELECT * FROM comment_segment")

relationship <- dbGetQuery(con, "SELECT * FROM comment_segment_relationship1")

x <- data.frame(segment)
y <- data.frame(relationship)

nodes <- data.frame(id = c(x$id), label = c(x$id),color = c(x$color), shape = c(x$shape))
edges <- data.frame(from = c(y$from), to = c(y$to))

visNetwork(nodes,edges,width = "100%",height = "500px")%>%
  visIgraphLayout() %>%
  visEdges(smooth = FALSE)

# print(x)
# print(y)

