a <- read.csv("../Data/site_Attr.csv",fileEncoding = "UTF-8-BOM" ,stringsAsFactors = FALSE)
b <- read.csv("../Data/site_Data.csv",fileEncoding = "UTF-8-BOM" ,stringsAsFactors = FALSE)
p <- read.csv("../Data/site_Relationship.csv",fileEncoding = "UTF-8-BOM",stringsAsFactors = FALSE)

z <- merge(x = a, y = b, by.x = c("id","type"),by.y = c("id","type"), all = TRUE)
str(z$id)
#print(y$site_name
nodes <- data.frame(id = c(z$id),shape = 'circle',group = c(z$type),label = c(z$id),font.size = 50)
edges <- data.frame(from = c(p$from), to = c(p$to))


visNetwork(nodes,edges,width = "100%",height = "500px")%>%
  visEdges(smooth = FALSE)
