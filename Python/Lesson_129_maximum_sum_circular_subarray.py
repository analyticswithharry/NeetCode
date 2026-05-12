# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 129 -- Maximum Sum Circular Subarray
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 65
# =============================================================
#
# QUESTION:
#   Given a circular integer array, find the maximum subarray sum (subarray may wrap).
# =============================================================
def maxCirc(a):
    tot=0; mxc=cur=a[0]; mnc=cur2=a[0]
    for i,x in enumerate(a):
        if i: cur=max(x,cur+x); mxc=max(mxc,cur); cur2=min(x,cur2+x); mnc=min(mnc,cur2)
        tot+=x
    return mxc if mxc<0 else max(mxc,tot-mnc)

if __name__=="__main__":
    print(maxCirc([1,-2,3,-2]))
    print(maxCirc([5,-3,5]))
    print(maxCirc([-3,-2,-3]))
