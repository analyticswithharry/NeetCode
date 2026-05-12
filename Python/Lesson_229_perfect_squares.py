# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 229 -- Perfect Squares
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 115
# =============================================================
#
# QUESTION:
#   Min number of perfect-square numbers summing to n.
# =============================================================
def numSquares(n):
    dp=[0]+[float('inf')]*n
    for i in range(1,n+1):
        j=1
        while j*j<=i: dp[i]=min(dp[i],dp[i-j*j]+1); j+=1
    return dp[n]
if __name__=="__main__":
    print(numSquares(12)); print(numSquares(13))
