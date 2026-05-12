# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 128 -- Reverse Integer
# Category   : Bit Manipulation
# Difficulty : Medium
# Study Plan : Day 64
# =============================================================
#
# QUESTION:
#   Reverse digits of a signed 32-bit integer; return 0 on overflow.
# =============================================================
def rev(x):
    s=-1 if x<0 else 1; x*=s; r=0
    while x: r=r*10+x%10; x//=10
    r*=s
    if r<-2**31 or r>2**31-1: return 0
    return r

if __name__=="__main__":
    print(rev(123)); print(rev(-456)); print(rev(1534236469))
