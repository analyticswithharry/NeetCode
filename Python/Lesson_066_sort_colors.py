# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 066 -- Sort Colors
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 33
# =============================================================
#
# QUESTION:
#   Sort an array containing only 0,1,2 in-place. Dutch National Flag.
#
#   Example: [2,0,2,1,1,0] -> [0,0,1,1,2,2]
# =============================================================

class Solution:
    def sortColors(self, nums):
        l, m, r = 0, 0, len(nums)-1
        while m <= r:
            if nums[m] == 0: nums[l], nums[m] = nums[m], nums[l]; l+=1; m+=1
            elif nums[m] == 2: nums[m], nums[r] = nums[r], nums[m]; r-=1
            else: m+=1
        return nums

if __name__ == "__main__":
    print(Solution().sortColors([2,0,2,1,1,0]))
