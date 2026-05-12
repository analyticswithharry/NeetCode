# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 226 -- Combination Sum IV
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 113
# =============================================================
#
# QUESTION:
#   Count ordered combinations of nums summing to target.
# =============================================================
def combSum4(nums,t):
    dp=[0]*(t+1); dp[0]=1
    for v in range(1,t+1):
        for x in nums:
            if v-x>=0: dp[v]+=dp[v-x]
    return dp[t]
if __name__=="__main__":
    print(combSum4([1,2,3],4))
