# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 159 -- Find Median From Data Stream
# Category   : Heap Priority Queue
# Difficulty : Hard
# Study Plan : Day 80
# =============================================================
#
# QUESTION:
#   Design MedianFinder: addNum, findMedian.
# =============================================================
MedianFinder <- function(){ lo<-c(); hi<-c(); add<-function(x){ lo<<-c(lo,x); lo<<-sort(lo,decreasing=TRUE); hi<<-c(hi,lo[1]); hi<<-sort(hi); lo<<-lo[-1]; if(length(hi)>length(lo)){ lo<<-c(hi[1],lo); lo<<-sort(lo,decreasing=TRUE); hi<<-hi[-1] } }; med<-function(){ if(length(lo)>length(hi)) lo[1] else (lo[1]+hi[1])/2 }; list(add=add,med=med) }
m<-MedianFinder(); for(x in c(1,2,3)){ m$add(x); cat(m$med(),"\n") }
