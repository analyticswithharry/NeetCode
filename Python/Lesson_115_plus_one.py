# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 115 -- Plus One
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 58
# =============================================================
#
# QUESTION:
#   Given a non-empty array of decimal digits representing a non-negative integer, add one and return the resulting array.
# =============================================================
def plusOne(d):
    d=d[:]
    for i in range(len(d)-1,-1,-1):
        if d[i]<9: d[i]+=1; return d
        d[i]=0
    return [1]+d

if __name__=="__main__":
    print(plusOne([1,2,3]))
    print(plusOne([9,9]))
