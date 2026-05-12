# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 001 -- Reverse String
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 1
# =============================================================
#
# QUESTION:
#   Write a function that reverses a string. The input string is given as
#   an array of characters s. You must do this by modifying the input array
#   in-place with O(1) extra memory.
#
#   Example:
#     Input : s = ['h','e','l','l','o']
#     Output: ['o','l','l','e','h']
# =============================================================

class Solution:
    def reverseString(self, s: list) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    s = list("hello")
    Solution().reverseString(s)
    print(s)  # ['o','l','l','e','h']
