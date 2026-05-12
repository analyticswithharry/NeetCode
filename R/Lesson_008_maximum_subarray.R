# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 008 -- Maximum Subarray
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 4
# =============================================================
#
# QUESTION:
#   Given an integer array nums, find the contiguous subarray (containing
#   at least one number) which has the largest sum and return its sum.
#
#   Example:
#     Input : nums = [-2,1,-3,4,-1,2,1,-5,4]
#     Output: 6   (subarray [4,-1,2,1])
# =============================================================

maxSubArray <- function(nums) {
    best <- nums[1]; cur <- nums[1]
    for (i in 2:length(nums)) { cur <- max(nums[i], cur + nums[i]); best <- max(best, cur) }
    best
}

print(maxSubArray(c(-2,1,-3,4,-1,2,1,-5,4)))  # 6
