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

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[m] < target: l = m + 1
            else: r = m - 1
        return -1

if __name__ == "__main__":
    print(Solution().search([-1,0,3,5,9,12], 9))  # 4
