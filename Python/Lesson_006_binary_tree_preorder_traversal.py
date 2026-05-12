# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 006 -- Binary Tree Preorder Traversal
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 3
# =============================================================
#
# QUESTION:
#   Given the root of a binary tree, return the preorder (Root, Left, Right)
#   traversal of its nodes' values.
#
#   Example:
#     Input : root = [1,null,2,3]
#     Output: [1, 2, 3]
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def preorderTraversal(self, root):
        if not root: return []
        out, st = [], [root]
        while st:
            n = st.pop(); out.append(n.val)
            if n.right: st.append(n.right)
            if n.left:  st.append(n.left)
        return out

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(Solution().preorderTraversal(root))  # [1, 2, 3]
