# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 078 -- Same Tree
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 39
# =============================================================
#
# QUESTION:
#   Given two binary trees, check if they are structurally identical with same node values.
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    c = TreeNode(1, TreeNode(2))
    print(Solution().isSameTree(a, b)); print(Solution().isSameTree(a, c))
