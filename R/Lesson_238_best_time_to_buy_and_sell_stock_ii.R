# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 238 -- Best Time to Buy And Sell Stock II
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 119
# =============================================================
#
# QUESTION:
#   Multiple transactions allowed. Sum positive deltas.
# =============================================================
maxProfit <- function(p){ d<-diff(p); sum(d[d>0]) }
cat(maxProfit(c(7,1,5,3,6,4)),"\n")
