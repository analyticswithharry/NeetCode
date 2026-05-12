# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 139 -- Roman to Integer
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 70
# =============================================================
#
# QUESTION:
#   Convert Roman numeral string to integer.
# =============================================================
def r2i(s):
    m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}; t=0; p=0
    for c in reversed(s):
        v=m[c]
        if v<p: t-=v
        else: t+=v; p=v
    return t

if __name__=="__main__":
    print(r2i("III")); print(r2i("LVIII")); print(r2i("MCMXCIV"))
