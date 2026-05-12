# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 064 -- Move Zeroes
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 32
# =============================================================
#
# QUESTION:
#   Move all 0s to the end while maintaining relative order. In-place.
#
#   Example: [0,1,0,3,12] -> [1,3,12,0,0]
# =============================================================

moveZeroes <- function(nums){ z <- nums[nums!=0]; c(z, rep(0, length(nums)-length(z))) }
print(moveZeroes(c(0,1,0,3,12)))
