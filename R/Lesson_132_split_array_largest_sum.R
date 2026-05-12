# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 132 -- Split Array Largest Sum
# Category   : Binary Search
# Difficulty : Hard
# Study Plan : Day 66
# =============================================================
#
# QUESTION:
#   Split nums into k non-empty contiguous parts to minimize the largest sum among parts.
# =============================================================
split2 <- function(a,k){ can<-function(mx){ c<-1; s<-0; for(x in a){ if(s+x>mx){ c<-c+1; s<-x } else s<-s+x }; c<=k }; lo<-max(a); hi<-sum(a); while(lo<hi){ m<-(lo+hi)%/%2; if(can(m)) hi<-m else lo<-m+1 }; lo }
cat(split2(c(7,2,5,10,8),2),"\n")
