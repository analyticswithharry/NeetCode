# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 241 -- First Missing Positive
# Category   : Arrays and Hashing
# Difficulty : Hard
# Study Plan : Day 121
# =============================================================
#
# QUESTION:
#   Smallest missing positive int. O(n) time, O(1) extra space (cyclic placement).
# =============================================================
def firstMissing(n):
    N=len(n)
    for i in range(N):
        while 1<=n[i]<=N and n[n[i]-1]!=n[i]:
            n[n[i]-1],n[i]=n[i],n[n[i]-1]
    for i in range(N):
        if n[i]!=i+1: return i+1
    return N+1
if __name__=="__main__":
    print(firstMissing([3,4,-1,1])); print(firstMissing([1,2,0]))
