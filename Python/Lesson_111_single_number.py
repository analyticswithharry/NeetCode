# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 111 -- Single Number
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 56
# =============================================================
#
# QUESTION:
#   Given a non-empty array of integers, every element appears twice except for one. Find that single one. O(1) extra space.
# =============================================================
def single(nums):
    r = 0
    for x in nums: r ^= x
    return r

if __name__ == "__main__":
    print(single([2,2,1]))
    print(single([4,1,2,1,2]))
