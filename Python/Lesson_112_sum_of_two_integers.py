# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 112 -- Sum of Two Integers
# Category   : Bit Manipulation
# Difficulty : Medium
# Study Plan : Day 56
# =============================================================
#
# QUESTION:
#   Given two integers a and b, return the sum without using + or -.
# =============================================================
def add(a,b):
    M=0xFFFFFFFF
    while b & M:
        c=((a & b) << 1) & M
        a=(a ^ b) & M
        b=c
    return a if a<=0x7FFFFFFF else ~(a^M)

if __name__=="__main__":
    print(add(1,2)); print(add(-2,3))
