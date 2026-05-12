# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 237 -- Longest Consecutive Sequence
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 119
# =============================================================
#
# QUESTION:
#   Length of longest run of consecutive integers in unsorted array. O(n) hashset.
# =============================================================
longestConsec <- function(n){ s<-unique(n); best<-0; for(x in s) if(!(x-1) %in% s){ y<-x; while((y+1) %in% s) y<-y+1; best<-max(best,y-x+1) }; best }
cat(longestConsec(c(100,4,200,1,3,2)),"\n")
