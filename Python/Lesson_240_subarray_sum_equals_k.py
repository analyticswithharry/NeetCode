# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 240 -- Subarray Sum Equals K
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 120
# =============================================================
#
# QUESTION:
#   Count subarrays with sum k using prefix-sum frequency map.
# =============================================================
def subarraySum(n,k):
    cnt=0; s=0; m={0:1}
    for x in n:
        s+=x; cnt+=m.get(s-k,0); m[s]=m.get(s,0)+1
    return cnt
if __name__=="__main__":
    print(subarraySum([1,1,1],2)); print(subarraySum([1,2,3],3))
