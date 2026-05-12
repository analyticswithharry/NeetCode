# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 067 -- Reverse Vowels of a String
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 34
# =============================================================
#
# QUESTION:
#   Reverse only the vowels of a string. Vowels: a,e,i,o,u (and uppercase).
#
#   Example: hello -> holle
# =============================================================

class Solution:
    def reverseVowels(self, s):
        v = set("aeiouAEIOU"); a = list(s); l,r = 0, len(a)-1
        while l < r:
            while l < r and a[l] not in v: l += 1
            while l < r and a[r] not in v: r -= 1
            a[l], a[r] = a[r], a[l]; l += 1; r -= 1
        return "".join(a)

if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))
    print(Solution().reverseVowels("leetcode"))
