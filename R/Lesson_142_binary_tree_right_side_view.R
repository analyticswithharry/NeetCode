# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 142 -- Binary Tree Right Side View
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 71
# =============================================================
#
# QUESTION:
#   Return values seen from the right side of a binary tree.
# =============================================================
view <- function(root){ if(is.null(root)) return(c()); q<-list(root); res<-c(); while(length(q)>0){ n<-length(q); nq<-list(); for(i in 1:n){ x<-q[[i]]; if(i==n) res<-c(res,x$val); if(!is.null(x$l)) nq[[length(nq)+1]]<-x$l; if(!is.null(x$r)) nq[[length(nq)+1]]<-x$r }; q<-nq }; res }
TN <- function(v,l=NULL,r=NULL) list(val=v,l=l,r=r)
print(view(TN(1,TN(2,NULL,TN(5)),TN(3,NULL,TN(4)))))
