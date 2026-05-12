# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 223 -- Burst Balloons
# Category   : 2-D Dynamic Programming
# Difficulty : Hard
# Study Plan : Day 112
# =============================================================
#
# QUESTION:
#   Burst balloons; coins = nums[l]*nums[i]*nums[r]. Maximize total.
# =============================================================
def maxCoins(nums):
    a=[1]+nums+[1]; n=len(a)
    dp=[[0]*n for _ in range(n)]
    for L in range(2,n):
        for l in range(0,n-L):
            r=l+L
            for i in range(l+1,r):
                dp[l][r]=max(dp[l][r],dp[l][i]+dp[i][r]+a[l]*a[i]*a[r])
    return dp[0][n-1]
if __name__=="__main__":
    print(maxCoins([3,1,5,8]))
