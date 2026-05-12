# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 219 -- Find K Closest Elements
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 110
# =============================================================
#
# QUESTION:
#   Return k closest sorted ints to x (binary search the window).
# =============================================================
def findClosest(arr,k,x):
    l,r=0,len(arr)-k
    while l<r:
        m=(l+r)//2
        if x-arr[m]>arr[m+k]-x: l=m+1
        else: r=m
    return arr[l:l+k]
if __name__=="__main__":
    print(findClosest([1,2,3,4,5],4,3))
