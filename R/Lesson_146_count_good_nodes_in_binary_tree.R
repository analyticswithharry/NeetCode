# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 146 -- Count Good Nodes In Binary Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 73
# =============================================================
#
# QUESTION:
#   A node is good if no node on the root-to-node path has a value greater. Count good nodes.
# =============================================================
good <- function(root){ rec<-function(n,m){ if(is.null(n)) return(0); c<-if(n$val>=m) 1 else 0; nm<-max(m,n$val); c+rec(n$l,nm)+rec(n$r,nm) }; rec(root,-Inf) }
TN <- function(v,l=NULL,r=NULL) list(val=v,l=l,r=r)
cat(good(TN(3,TN(1,TN(3)),TN(4,TN(1),TN(5)))),"\n")
