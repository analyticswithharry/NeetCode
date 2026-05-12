# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 010 -- Search Insert Position
# Category   : Binary Search
# Difficulty : Easy
# Study Plan : Day 5
# =============================================================
#
# QUESTION:
#   Given a sorted array of distinct integers and a target, return the
#   index if the target is found. If not, return the index where it would
#   be inserted in order. Must run in O(log n).
#
#   Example:
#     Input : nums = [1,3,5,6], target = 5    Output: 2
#     Input : nums = [1,3,5,6], target = 2    Output: 1
# =============================================================

class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] < target: l = m + 1
            else: r = m
        return l

if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 5))  # 2
    print(Solution().searchInsert([1,3,5,6], 2))  # 1
