# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 061 -- Contains Duplicate
# Category   : Arrays and Hashing
# Difficulty : Easy
# Study Plan : Day 31
# =============================================================
#
# QUESTION:
#   Given an integer array nums, return true if any value appears at least twice.
#
#   Example: [1,2,3,1] -> true; [1,2,3,4] -> false
# =============================================================

class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

if __name__ == "__main__":
    print(Solution().containsDuplicate([1,2,3,1]))
    print(Solution().containsDuplicate([1,2,3,4]))
