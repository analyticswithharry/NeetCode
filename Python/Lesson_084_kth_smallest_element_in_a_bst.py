# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 084 -- Kth Smallest Element in a BST
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 42
# =============================================================
#
# QUESTION:
#   Given a BST, return the kth smallest value (1-indexed). Use inorder traversal.
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def kthSmallest(self, root, k):
        st, cur = [], root
        while st or cur:
            while cur: st.append(cur); cur = cur.left
            cur = st.pop(); k -= 1
            if k == 0: return cur.val
            cur = cur.right

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(Solution().kthSmallest(r, 1))
    print(Solution().kthSmallest(r, 3))
