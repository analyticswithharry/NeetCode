# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 127 -- Number of 1 Bits
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 64
# =============================================================
#
# QUESTION:
#   Return the number of 1 bits in unsigned int.
# =============================================================
def hw(n):
    c=0
    while n: n&=n-1; c+=1
    return c

if __name__=="__main__":
    print(hw(11)); print(hw(128))
