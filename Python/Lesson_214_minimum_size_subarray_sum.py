# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 214 -- Minimum Size Subarray Sum
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 107
# =============================================================
#
# QUESTION:
#   Return the minimum length of a contiguous subarray whose sum is >= target. 0 if none.
# =============================================================
def minSubArrayLen(t,nums):
    l=0; s=0; ans=float('inf')
    for r,x in enumerate(nums):
        s+=x
        while s>=t: ans=min(ans,r-l+1); s-=nums[l]; l+=1
    return 0 if ans==float('inf') else ans
if __name__=="__main__":
    print(minSubArrayLen(7,[2,3,1,2,4,3]))
    print(minSubArrayLen(11,[1,1,1,1,1,1]))
