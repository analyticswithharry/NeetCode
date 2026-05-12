# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 230 -- Integer Break
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 115
# =============================================================
#
# QUESTION:
#   Break n into >=2 positive ints; maximize product.
# =============================================================
def integerBreak(n):
    dp=[0]*(n+1); dp[1]=1
    for i in range(2,n+1):
        for j in range(1,i):
            dp[i]=max(dp[i],j*max(i-j,dp[i-j]))
    return dp[n]
if __name__=="__main__":
    print(integerBreak(2)); print(integerBreak(10))
