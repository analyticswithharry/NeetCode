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

class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0: nums[i], nums[j] = nums[j], nums[i]; j += 1
        return nums

if __name__ == "__main__":
    print(Solution().moveZeroes([0,1,0,3,12]))
