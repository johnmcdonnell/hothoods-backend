
library(reshape2)
library(data.table)

historical <- read.delim("subwayridership/historical_data.txt")
historical.firstnormal <- as.data.table(melt(historical, id=c("LineSegment", "Order", "Borough", "Station", "Old.Borough", "Old.Station", "Open.Date")))
historical.firstnormal[,year:=as.numeric(substr(variable, 2, 5))]
historical.firstnormal <- historical.firstnormal[value!=" - "]
historical.firstnormal[,riders:=as.numeric(gsub(",","", value))]

historical.reduced <- historical.firstnormal[,list(LineSegment, Order, Borough, Station, year, riders)]

write.table(historical.reduced, "subwayridership/historical_firstnormal.csv")

