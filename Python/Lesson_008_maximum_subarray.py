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

class Solution:
    def maxSubArray(self, nums):
        best = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best

if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
