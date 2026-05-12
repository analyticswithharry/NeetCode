# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 147 -- Last Stone Weight II
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 74
# =============================================================
#
# QUESTION:
#   Given stones, smash to minimize remaining weight (subset partition).
# =============================================================
def lsw2(s):
    t=sum(s); cap=t//2
    dp=[False]*(cap+1); dp[0]=True
    for x in s:
        for j in range(cap,x-1,-1): dp[j]=dp[j] or dp[j-x]
    for j in range(cap,-1,-1):
        if dp[j]: return t-2*j

if __name__=="__main__":
    print(lsw2([2,7,4,1,8,1])); print(lsw2([31,26,33,21,40]))
