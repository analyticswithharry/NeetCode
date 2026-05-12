# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 153 -- Walls And Gates
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 77
# =============================================================
#
# QUESTION:
#   Grid: -1 wall, 0 gate, INF empty. Fill each empty with distance to nearest gate.
# =============================================================
INF <- 2^31-1
walls <- function(g){ m<-nrow(g); n<-ncol(g); q<-list(); for(i in 1:m) for(j in 1:n) if(g[i,j]==0) q[[length(q)+1]]<-c(i,j); D<-list(c(-1,0),c(1,0),c(0,-1),c(0,1)); while(length(q)>0){ p<-q[[1]]; q<-q[-1]; for(d in D){ ni<-p[1]+d[1]; nj<-p[2]+d[2]; if(ni>=1 && nj>=1 && ni<=m && nj<=n && g[ni,nj]==INF){ g[ni,nj]<-g[p[1],p[2]]+1; q[[length(q)+1]]<-c(ni,nj) } } }; g }
g<-matrix(c(INF,-1,0,INF,INF,INF,INF,-1,INF,-1,INF,-1,0,-1,INF,INF),4,4,byrow=TRUE); print(walls(g))
