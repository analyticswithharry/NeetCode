# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 077 -- Find the Duplicate Number
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 39
# =============================================================
#
# QUESTION:
#   An array of n+1 integers in [1,n] has exactly one duplicate. Find it (Floyd cycle detection, O(n) time, O(1) space).
# =============================================================

findDuplicate <- function(nums){ t <- table(nums); as.integer(names(t)[t > 1]) }
print(findDuplicate(c(1,3,4,2,2)))
print(findDuplicate(c(3,1,3,4,2)))
