# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 124 -- Top K Frequent Elements
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 62
# =============================================================
#
# QUESTION:
#   Given an integer array nums and integer k, return the k most frequent elements.
# =============================================================
topK <- function(a,k){ t <- sort(table(a),decreasing=TRUE); as.integer(names(t)[1:k]) }
print(topK(c(1,1,1,2,2,3),2))
