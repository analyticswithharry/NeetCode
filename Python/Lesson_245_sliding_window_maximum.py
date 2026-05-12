# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 245 -- Sliding Window Maximum
# Category   : Sliding Window
# Difficulty : Hard
# Study Plan : Day 123
# =============================================================
#
# QUESTION:
#   Max in each window of size k. Monotonic deque.
# =============================================================
from collections import deque
def maxSliding(n,k):
    dq=deque(); out=[]
    for i,x in enumerate(n):
        while dq and n[dq[-1]]<=x: dq.pop()
        dq.append(i)
        if dq[0]<=i-k: dq.popleft()
        if i>=k-1: out.append(n[dq[0]])
    return out
if __name__=="__main__":
    print(maxSliding([1,3,-1,-3,5,3,6,7],3))
