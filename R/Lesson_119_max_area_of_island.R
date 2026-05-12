# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 119 -- Max Area of Island
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 60
# =============================================================
#
# QUESTION:
#   Given m x n binary grid, return max area of an island (4-directionally connected 1s).
# =============================================================
maxArea <- function(g){ m<-nrow(g); n<-ncol(g); dfs <- function(i,j){ if(i<1||j<1||i>m||j>n||g[i,j]!=1) return(0); g[i,j] <<- 0; 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1) }; b<-0; for(i in 1:m) for(j in 1:n) if(g[i,j]==1) b<-max(b,dfs(i,j)); b }
g <- matrix(c(1,1,0,1,0,0,0,0,1),3,3,byrow=TRUE); cat(maxArea(g),"\n")
