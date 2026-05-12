# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 225 -- Partition Equal Subset Sum
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 113
# =============================================================
#
# QUESTION:
#   Can the array be split into two equal-sum subsets? Subset-sum DP.
# =============================================================
def canPartition(nums):
    s=sum(nums)
    if s%2: return False
    t=s//2
    dp={0}
    for x in nums:
        dp |= {v+x for v in dp if v+x<=t}
        if t in dp: return True
    return t in dp
if __name__=="__main__":
    print(canPartition([1,5,11,5]))
    print(canPartition([1,2,3,5]))
