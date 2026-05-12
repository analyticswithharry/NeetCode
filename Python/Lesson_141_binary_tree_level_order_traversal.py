# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 141 -- Binary Tree Level Order Traversal
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 71
# =============================================================
#
# QUESTION:
#   Return level-order traversal of a binary tree (values grouped by level).
# =============================================================
from collections import deque
class TN:
    def __init__(self,v,l=None,r=None): self.val=v; self.left=l; self.right=r
def levels(root):
    if not root: return []
    q=deque([root]); res=[]
    while q:
        lvl=[]
        for _ in range(len(q)):
            n=q.popleft(); lvl.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        res.append(lvl)
    return res

if __name__=="__main__":
    r=TN(3,TN(9),TN(20,TN(15),TN(7)))
    print(levels(r))
