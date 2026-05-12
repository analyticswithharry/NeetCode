# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 144 -- Decode Ways
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 72
# =============================================================
#
# QUESTION:
#   Number of ways to decode digit string s where '1'->A, ..., '26'->Z.
# =============================================================
def ways(s):
    if not s or s[0]=='0': return 0
    n=len(s); dp=[0]*(n+1); dp[0]=dp[1]=1
    for i in range(2,n+1):
        if s[i-1]!='0': dp[i]+=dp[i-1]
        x=int(s[i-2:i])
        if 10<=x<=26: dp[i]+=dp[i-2]
    return dp[n]

if __name__=="__main__":
    print(ways("12")); print(ways("226")); print(ways("06"))
