# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 009 -- Binary Search
# Category   : Binary Search
# Difficulty : Easy
# Study Plan : Day 5
# =============================================================
#
# QUESTION:
#   Given a sorted (ascending) array of integers nums and a target, return
#   the index of target if it exists, otherwise -1. You must run in O(log n).
#
#   Example:
#     Input : nums = [-1,0,3,5,9,12], target = 9
#     Output: 4
# =============================================================

binarySearch <- function(nums, target) {
    l <- 1; r <- length(nums)
    while (l <= r) {
        m <- (l + r) %/% 2
        if (nums[m] == target) return(m - 1L)  # 0-based
        if (nums[m] < target) l <- m + 1 else r <- m - 1
    }
    -1L
}

print(binarySearch(c(-1,0,3,5,9,12), 9))  # 4
