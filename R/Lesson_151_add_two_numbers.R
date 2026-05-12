# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 151 -- Add Two Numbers
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 76
# =============================================================
#
# QUESTION:
#   Two non-empty linked lists (least-significant-digit first). Add and return sum as linked list.
# =============================================================
add <- function(a,b){ res<-c(); c<-0; i<-1; while(i<=max(length(a),length(b)) || c>0){ v<-c+if(i<=length(a)) a[i] else 0+if(i<=length(b)) b[i] else 0; res<-c(res,v%%10); c<-v%/%10; i<-i+1 }; res }
print(add(c(2,4,3),c(5,6,4)))
