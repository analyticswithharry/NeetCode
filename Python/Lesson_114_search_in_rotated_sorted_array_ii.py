# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 114 -- Search In Rotated Sorted Array II
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 57
# =============================================================
#
# QUESTION:
#   Rotated sorted array may contain duplicates. Return true if target exists.
# =============================================================
def search(a,t):
    lo,hi=0,len(a)-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==t: return True
        if a[lo]==a[m]==a[hi]: lo+=1; hi-=1
        elif a[lo]<=a[m]:
            if a[lo]<=t<a[m]: hi=m-1
            else: lo=m+1
        else:
            if a[m]<t<=a[hi]: lo=m+1
            else: hi=m-1
    return False

if __name__=="__main__":
    print(search([2,5,6,0,0,1,2],0))
    print(search([2,5,6,0,0,1,2],3))
