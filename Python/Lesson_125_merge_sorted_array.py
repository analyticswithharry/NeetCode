# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 125 -- Merge Sorted Array
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 63
# =============================================================
#
# QUESTION:
#   Given nums1 (length m+n) and nums2 (length n) sorted, merge nums2 into nums1 in-place sorted.
# =============================================================
def merge(a,m,b,n):
    i,j,k=m-1,n-1,m+n-1
    while j>=0:
        if i>=0 and a[i]>b[j]: a[k]=a[i]; i-=1
        else: a[k]=b[j]; j-=1
        k-=1
    return a

if __name__=="__main__":
    print(merge([1,2,3,0,0,0],3,[2,5,6],3))
