# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 247 -- Remove Duplicates From Sorted Array
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 124
# =============================================================
#
# QUESTION:
#   In-place dedupe of sorted array. Return new length.
# =============================================================
def dedupe(a):
    if not a: return 0
    k=1
    for i in range(1,len(a)):
        if a[i]!=a[k-1]: a[k]=a[i]; k+=1
    return k
if __name__=="__main__":
    a=[1,1,2,2,3]; n=dedupe(a); print(n,a[:n])
