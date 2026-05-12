# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 126 -- Container With Most Water
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 63
# =============================================================
#
# QUESTION:
#   Given heights, find two lines that form the container holding most water.
# =============================================================
def maxArea(h):
    l,r=0,len(h)-1; b=0
    while l<r:
        b=max(b,(r-l)*min(h[l],h[r]))
        if h[l]<h[r]: l+=1
        else: r-=1
    return b

if __name__=="__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))
