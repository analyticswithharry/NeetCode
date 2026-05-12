# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 079 -- Subtree of Another Tree
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 40
# =============================================================
#
# QUESTION:
#   Given roots of two trees root and subRoot, return true if subRoot is a subtree of root.
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSubtree(self, root, sub):
        if not root: return False
        if self.isSameTree(root, sub): return True
        return self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub)

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    s = TreeNode(4, TreeNode(1), TreeNode(2))
    print(Solution().isSubtree(r, s))
