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

class Solution:
    def sortedSquares(self, nums):
        n = len(nums); out = [0]*n
        l, r, k = 0, n-1, n-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]): out[k] = nums[l]*nums[l]; l += 1
            else: out[k] = nums[r]*nums[r]; r -= 1
            k -= 1
        return out

if __name__ == "__main__":
    print(Solution().sortedSquares([-4,-1,0,3,10]))
