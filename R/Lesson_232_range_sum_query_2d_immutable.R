# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 232 -- Range Sum Query 2D Immutable
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 116
# =============================================================
#
# QUESTION:
#   Build prefix sum 2D for O(1) region queries.
# =============================================================
sumRegion <- function(m,r1,c1,r2,c2){ R<-nrow(m); C<-ncol(m); p<-matrix(0,R+1,C+1); for(i in 1:R) for(j in 1:C) p[i+1,j+1]<-m[i,j]+p[i,j+1]+p[i+1,j]-p[i,j]; p[r2+2,c2+2]-p[r1+1,c2+2]-p[r2+2,c1+1]+p[r1+1,c1+1] }
cat(sumRegion(matrix(c(3,0,1,5,6,3,1,2,0),3,3,byrow=TRUE),0,0,2,2),"\n")
