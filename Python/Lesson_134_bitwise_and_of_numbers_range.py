# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 134 -- Bitwise AND of Numbers Range
# Category   : Bit Manipulation
# Difficulty : Medium
# Study Plan : Day 67
# =============================================================
#
# QUESTION:
#   Given range [m,n], return the bitwise AND of all numbers in this range, inclusive.
# =============================================================
def rangeAnd(m,n):
    s=0
    while m!=n: m>>=1; n>>=1; s+=1
    return m<<s

if __name__=="__main__":
    print(rangeAnd(5,7)); print(rangeAnd(0,0))
