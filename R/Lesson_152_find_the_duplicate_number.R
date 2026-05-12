# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 152 -- Find The Duplicate Number
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 76
# =============================================================
#
# QUESTION:
#   Array length n+1 with values in [1,n] containing one duplicate. Find it. O(1) extra space.
# =============================================================
dup <- function(a){ s<-a[1]; f<-a[1]; repeat { s<-a[s+1]; f<-a[a[f+1]+1]; if(s==f) break }; s<-a[1]; while(s!=f){ s<-a[s+1]; f<-a[f+1] }; s }
cat(dup(c(1,3,4,2,2)),"\n"); cat(dup(c(3,1,3,4,2)),"\n")
