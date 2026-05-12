# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 239 -- Majority Element II
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 120
# =============================================================
#
# QUESTION:
#   All elements appearing more than n/3 times. Boyer-Moore variant.
# =============================================================
majorityIII <- function(nums){ t<-table(nums); as.integer(names(t[t>length(nums)/3])) }
cat(majorityIII(c(1,1,1,3,3,2,2,2)),"\n")
