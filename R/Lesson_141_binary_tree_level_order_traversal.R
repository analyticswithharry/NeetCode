# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 141 -- Binary Tree Level Order Traversal
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 71
# =============================================================
#
# QUESTION:
#   Return level-order traversal of a binary tree (values grouped by level).
# =============================================================
levels <- function(root){ if(is.null(root)) return(list()); q<-list(root); res<-list(); while(length(q)>0){ lvl<-c(); nq<-list(); for(x in q){ lvl<-c(lvl,x$val); if(!is.null(x$l)) nq[[length(nq)+1]]<-x$l; if(!is.null(x$r)) nq[[length(nq)+1]]<-x$r }; q<-nq; res[[length(res)+1]]<-lvl }; res }
TN <- function(v,l=NULL,r=NULL) list(val=v,l=l,r=r)
print(levels(TN(3,TN(9),TN(20,TN(15),TN(7)))))
