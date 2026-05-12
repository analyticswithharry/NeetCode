# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 235 -- Product of Array Except Self
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 118
# =============================================================
#
# QUESTION:
#   Return array where output[i] = product of all nums except nums[i]. O(n) no division.
# =============================================================
productExceptSelf <- function(n){ o<-rep(1,length(n)); p<-1; for(i in seq_along(n)){ o[i]<-p; p<-p*n[i] }; p<-1; for(i in length(n):1){ o[i]<-o[i]*p; p<-p*n[i] }; o }
cat(productExceptSelf(c(1,2,3,4)),"\n")
