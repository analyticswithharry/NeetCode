# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 241 -- First Missing Positive
# Category   : Arrays and Hashing
# Difficulty : Hard
# Study Plan : Day 121
# =============================================================
#
# QUESTION:
#   Smallest missing positive int. O(n) time, O(1) extra space (cyclic placement).
# =============================================================
firstMissing <- function(n){ N<-length(n); s<-setdiff(1:(N+1),n); min(s) }
cat(firstMissing(c(3,4,-1,1)),"\n")
