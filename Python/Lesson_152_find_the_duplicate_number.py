# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 152 -- Find The Duplicate Number
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 76
# =============================================================
#
# QUESTION:
#   Array length n+1 with values in [1,n] containing one duplicate. Find it. O(1) extra space.
# =============================================================
def dup(a):
    s=f=a[0]
    while True:
        s=a[s]; f=a[a[f]]
        if s==f: break
    s=a[0]
    while s!=f: s=a[s]; f=a[f]
    return s

if __name__=="__main__":
    print(dup([1,3,4,2,2])); print(dup([3,1,3,4,2]))
