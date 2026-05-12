# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 068 -- Best Time to Buy and Sell Stock II
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 34
# =============================================================
#
# QUESTION:
#   You may complete as many transactions as you like (buy then sell). Return max profit.
#
#   Example: [7,1,5,3,6,4] -> 7  (buy 1 sell 5, buy 3 sell 6)
# =============================================================

maxProfit <- function(prices){
    d <- diff(prices); sum(d[d>0])
}
print(maxProfit(c(7,1,5,3,6,4)))
