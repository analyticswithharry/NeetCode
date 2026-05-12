# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 133 -- Counting Bits
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 67
# =============================================================
#
# QUESTION:
#   For 0..n return array where ans[i] = number of 1-bits in i.
# =============================================================
def cb(n):
    a=[0]*(n+1)
    for i in range(1,n+1): a[i]=a[i>>1]+(i&1)
    return a

if __name__=="__main__":
    print(cb(5))
