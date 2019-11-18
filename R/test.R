y <- read.csv("site_Attr.csv",fileEncoding = "UTF-8-BOM")
print(y$id)
nodes <- data.frame(id = y$id,label = c(y$p_Attr),font.size = 50,shape = 'circle')
visNetwork(nodes,width = "100%")

