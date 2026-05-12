# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 081 -- Binary Tree Right Side View
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 41
# =============================================================
#
# QUESTION:
#   Return the values of nodes you'd see ordered from top to bottom from the right side.
#
#   Example: [1,2,3,null,5,null,4] -> [1,3,4]
# =============================================================

from collections import deque
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def rightSideView(self, root):
        if not root: return []
        out, q = [], deque([root])
        while q:
            n = len(q)
            for i in range(n):
                x = q.popleft()
                if i == n-1: out.append(x.val)
                if x.left: q.append(x.left)
                if x.right: q.append(x.right)
        return out

if __name__ == "__main__":
    r = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(Solution().rightSideView(r))
