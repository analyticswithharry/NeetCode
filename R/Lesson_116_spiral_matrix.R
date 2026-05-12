# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 116 -- Spiral Matrix
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 58
# =============================================================
#
# QUESTION:
#   Given m x n matrix, return all elements in spiral order.
# =============================================================
spiral <- function(m){ r<-c(); if(length(m)==0) return(r); t<-1;b<-nrow(m);l<-1;rg<-ncol(m); while(t<=b && l<=rg){ for(j in l:rg) r<-c(r,m[t,j]); t<-t+1; if(t<=b) for(i in t:b) r<-c(r,m[i,rg]); rg<-rg-1; if(t<=b && l<=rg) for(j in rg:l) r<-c(r,m[b,j]); b<-b-1; if(l<=rg && t<=b) for(i in b:t) r<-c(r,m[i,l]); l<-l+1 }; r }
print(spiral(matrix(1:9,3,3,byrow=TRUE)))
