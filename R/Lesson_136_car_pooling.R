# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 136 -- Car Pooling
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 68
# =============================================================
#
# QUESTION:
#   Trips [numPassengers,from,to]; capacity. Return true iff possible to pick up & drop off all passengers without exceeding capacity.
# =============================================================
carPool <- function(t,cap){ e<-rep(0,1001); for(x in t){ e[x[2]+1]<-e[x[2]+1]+x[1]; e[x[3]+1]<-e[x[3]+1]-x[1] }; s<-0; for(v in e){ s<-s+v; if(s>cap) return(FALSE) }; TRUE }
cat(carPool(list(c(2,1,5),c(3,3,7)),4),"\n"); cat(carPool(list(c(2,1,5),c(3,3,7)),5),"\n")
