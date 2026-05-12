# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 080 -- Binary Tree Level Order Traversal
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 40
# =============================================================
#
# QUESTION:
#   Return level-order traversal of a binary tree as list of lists.
#
#   Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
# =============================================================

from collections import deque
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def levelOrder(self, root):
        if not root: return []
        out, q = [], deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                n = q.popleft(); level.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            out.append(level)
        return out

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().levelOrder(r))
