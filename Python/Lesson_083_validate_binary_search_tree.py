# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 083 -- Validate Binary Search Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 42
# =============================================================
#
# QUESTION:
#   Given the root of a binary tree, determine if it is a valid BST.
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def isValidBST(self, root):
        def go(n, lo, hi):
            if not n: return True
            if n.val <= lo or n.val >= hi: return False
            return go(n.left, lo, n.val) and go(n.right, n.val, hi)
        return go(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    r = TreeNode(2, TreeNode(1), TreeNode(3))
    bad = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(Solution().isValidBST(r)); print(Solution().isValidBST(bad))
