# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 154 -- Rotting Oranges
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 77
# =============================================================
#
# QUESTION:
#   0 empty, 1 fresh, 2 rotten. Each minute rotten infects 4-neighbor fresh. Min minutes to rot all, or -1.
# =============================================================
rot <- function(g){ m<-nrow(g); n<-ncol(g); q<-list(); fresh<-0; for(i in 1:m) for(j in 1:n){ if(g[i,j]==2) q[[length(q)+1]]<-c(i,j,0) else if(g[i,j]==1) fresh<-fresh+1 }; t<-0; D<-list(c(-1,0),c(1,0),c(0,-1),c(0,1)); while(length(q)>0){ p<-q[[1]]; q<-q[-1]; t<-p[3]; for(d in D){ ni<-p[1]+d[1]; nj<-p[2]+d[2]; if(ni>=1 && nj>=1 && ni<=m && nj<=n && g[ni,nj]==1){ g[ni,nj]<-2; fresh<-fresh-1; q[[length(q)+1]]<-c(ni,nj,p[3]+1) } } }; if(fresh>0) -1 else t }
cat(rot(matrix(c(2,1,1,1,1,0,0,1,1),3,3,byrow=TRUE)),"\n"); cat(rot(matrix(c(2,1,1,0,1,1,1,0,1),3,3,byrow=TRUE)),"\n")
