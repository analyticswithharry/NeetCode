# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 113 -- Search In Rotated Sorted Array
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 57
# =============================================================
#
# QUESTION:
#   Given a rotated sorted array (no duplicates) and target, return index or -1. O(log n).
# =============================================================
def search(a,t):
    lo,hi=0,len(a)-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==t: return m
        if a[lo]<=a[m]:
            if a[lo]<=t<a[m]: hi=m-1
            else: lo=m+1
        else:
            if a[m]<t<=a[hi]: lo=m+1
            else: hi=m-1
    return -1

if __name__=="__main__":
    print(search([4,5,6,7,0,1,2],0))
    print(search([4,5,6,7,0,1,2],3))
