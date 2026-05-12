# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 065 -- Squares of a Sorted Array
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 33
# =============================================================
#
# QUESTION:
#   Given a sorted (non-decreasing) array, return an array of squares of each number, also sorted.
#
#   Example: [-4,-1,0,3,10] -> [0,1,9,16,100]
# =============================================================

sortedSquares <- function(nums) sort(nums*nums)
print(sortedSquares(c(-4,-1,0,3,10)))
