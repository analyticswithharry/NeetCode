# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 222 -- Candy
# Category   : Greedy
# Difficulty : Hard
# Study Plan : Day 111
# =============================================================
#
# QUESTION:
#   Each child gets >=1 candy; higher rating gets more than neighbors. Return min candies.
# =============================================================
def candy(r):
    n=len(r); a=[1]*n
    for i in range(1,n):
        if r[i]>r[i-1]: a[i]=a[i-1]+1
    for i in range(n-2,-1,-1):
        if r[i]>r[i+1]: a[i]=max(a[i],a[i+1]+1)
    return sum(a)
if __name__=="__main__":
    print(candy([1,0,2]))
    print(candy([1,2,2]))
