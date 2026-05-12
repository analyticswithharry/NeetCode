# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 077 -- Find the Duplicate Number
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 39
# =============================================================
#
# QUESTION:
#   An array of n+1 integers in [1,n] has exactly one duplicate. Find it (Floyd cycle detection, O(n) time, O(1) space).
# =============================================================

class Solution:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]; fast = nums[nums[fast]]
            if slow == fast: break
        slow = nums[0]
        while slow != fast: slow = nums[slow]; fast = nums[fast]
        return slow

if __name__ == "__main__":
    print(Solution().findDuplicate([1,3,4,2,2]))
    print(Solution().findDuplicate([3,1,3,4,2]))
