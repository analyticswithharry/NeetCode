# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 140 -- Set Matrix Zeroes
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 70
# =============================================================
#
# QUESTION:
#   Given m x n matrix, if an element is 0, set its entire row and column to 0. In place.
# =============================================================
setZero <- function(g){ m<-nrow(g); n<-ncol(g); r0<-any(g[1,]==0); c0<-any(g[,1]==0); for(i in 2:m) for(j in 2:n) if(g[i,j]==0){ g[i,1]<-0; g[1,j]<-0 }; for(i in 2:m) for(j in 2:n) if(g[i,1]==0 || g[1,j]==0) g[i,j]<-0; if(r0) g[1,]<-0; if(c0) g[,1]<-0; g }
print(setZero(matrix(c(1,1,1,1,0,1,1,1,1),3,3,byrow=TRUE)))
