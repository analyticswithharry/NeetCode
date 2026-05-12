# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 224 -- Regular Expression Matching
# Category   : 2-D Dynamic Programming
# Difficulty : Hard
# Study Plan : Day 112
# =============================================================
#
# QUESTION:
#   Implement regex with '.' and '*' (zero or more of preceding).
# =============================================================
def isMatch(s,p):
    m,n=len(s),len(p)
    dp=[[False]*(n+1) for _ in range(m+1)]
    dp[0][0]=True
    for j in range(1,n+1):
        if p[j-1]=='*': dp[0][j]=dp[0][j-2]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[j-1]=='.' or p[j-1]==s[i-1]: dp[i][j]=dp[i-1][j-1]
            elif p[j-1]=='*':
                dp[i][j]=dp[i][j-2] or ((p[j-2]=='.' or p[j-2]==s[i-1]) and dp[i-1][j])
    return dp[m][n]
if __name__=="__main__":
    print(isMatch("aa","a*"))
    print(isMatch("ab",".*"))
