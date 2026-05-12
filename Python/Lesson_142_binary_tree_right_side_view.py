# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 142 -- Binary Tree Right Side View
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 71
# =============================================================
#
# QUESTION:
#   Return values seen from the right side of a binary tree.
# =============================================================
from collections import deque
class TN:
    def __init__(self,v,l=None,r=None): self.val=v; self.left=l; self.right=r
def view(root):
    if not root: return []
    q=deque([root]); res=[]
    while q:
        n=len(q)
        for i in range(n):
            x=q.popleft()
            if i==n-1: res.append(x.val)
            if x.left: q.append(x.left)
            if x.right: q.append(x.right)
    return res

if __name__=="__main__":
    r=TN(1,TN(2,None,TN(5)),TN(3,None,TN(4)))
    print(view(r))
