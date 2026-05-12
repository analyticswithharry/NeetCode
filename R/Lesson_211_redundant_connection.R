# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 211 -- Redundant Connection
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 106
# =============================================================
#
# QUESTION:
#   Given an n-node tree with one extra edge (forming exactly one cycle), return the edge that can be removed.
# =============================================================
findRedundant <- function(e){ n<-length(e); p<-0:n; f<-function(x){ while(p[x+1]!=x){ p[x+1]<<-p[p[x+1]+1]; x<-p[x+1] }; x }; for(x in e){ ra<-f(x[1]); rb<-f(x[2]); if(ra==rb) return(x); p[ra+1]<<-rb }; NULL }
cat(findRedundant(list(c(1,2),c(1,3),c(2,3))),"\n")
