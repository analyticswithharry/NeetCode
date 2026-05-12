# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 145 -- Construct Quad Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 73
# =============================================================
#
# QUESTION:
#   Given an n x n grid of 0/1, build a quad tree representation. Return root.
# =============================================================
build <- function(g){ rec <- function(r,c,n){ sub<-g[r:(r+n-1),c:(c+n-1),drop=FALSE]; if(length(unique(as.vector(sub)))==1) return(list(val=g[r,c],leaf=TRUE)); h<-n/2; list(leaf=FALSE,tl=rec(r,c,h),tr=rec(r,c+h,h),bl=rec(r+h,c,h),br=rec(r+h,c+h,h)) }; rec(1,1,nrow(g)) }
ser <- function(n){ if(isTRUE(n$leaf)) return(as.character(n$val)); c("#",ser(n$tl),ser(n$tr),ser(n$bl),ser(n$br)) }
print(ser(build(matrix(c(0,1,1,0),2,2,byrow=TRUE))))
