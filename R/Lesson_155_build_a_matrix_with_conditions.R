# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 155 -- Build a Matrix With Conditions
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 78
# =============================================================
#
# QUESTION:
#   Given k rows/cols and conditions for row/col orderings, place 1..k so each appears once and conditions are satisfied. Return matrix or [].
# =============================================================
topo <- function(k,conds){ adj<-vector("list",k); ind<-rep(0,k); for(c in conds){ adj[[c[1]]]<-c(adj[[c[1]]],c[2]); ind[c[2]]<-ind[c[2]]+1 }; q<-which(ind==0); o<-c(); while(length(q)>0){ x<-q[1]; q<-q[-1]; o<-c(o,x); for(y in adj[[x]]){ ind[y]<-ind[y]-1; if(ind[y]==0) q<-c(q,y) } }; if(length(o)==k) o else c() }
build <- function(k,rC,cC){ r<-topo(k,rC); c<-topo(k,cC); if(length(r)==0 || length(c)==0) return(matrix(0,0,0)); pos<-rep(0,k); for(i in seq_along(c)) pos[c[i]]<-i; g<-matrix(0,k,k); for(i in seq_along(r)) g[i,pos[r[i]]]<-r[i]; g }
print(build(3,list(c(1,2),c(3,2)),list(c(2,1),c(3,2))))
