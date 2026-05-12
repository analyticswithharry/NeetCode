# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 158 -- Minimum Array End
# Category   : Bit Manipulation
# Difficulty : Medium
# Study Plan : Day 79
# =============================================================
#
# QUESTION:
#   Given n and x, return min possible value v such that AND of n distinct integers (>=x, <=v, all sharing bits of x) equals x. Equivalent: spread (n-1) over the zero-bits of x.
# =============================================================
def minEnd(n,x):
    n-=1; r=x; bit=1; nb=1
    while nb<=n:
        if not (x & bit):
            if n & nb: r |= bit
            nb<<=1
        bit<<=1
    return r

if __name__=="__main__":
    print(minEnd(3,4)); print(minEnd(2,7))
