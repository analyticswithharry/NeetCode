# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 002 -- Two Sum II Input Array Is Sorted
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 1
# =============================================================
#
# QUESTION:
#   Given a 1-indexed sorted array of integers `numbers`, find two numbers
#   such that they add up to a specific `target`. Return their 1-based
#   indices as [index1, index2]. Use O(1) extra space.
#
#   Example:
#     Input : numbers = [2,7,11,15], target = 9
#     Output: [1,2]   (because 2 + 7 = 9)
# =============================================================

twoSum <- function(numbers, target) {
    l <- 1; r <- length(numbers)
    while (l < r) {
        s <- numbers[l] + numbers[r]
        if (s == target) return(c(l, r))
        if (s < target) l <- l + 1 else r <- r - 1
    }
    integer(0)
}

print(twoSum(c(2,7,11,15), 9))  # 1 2
