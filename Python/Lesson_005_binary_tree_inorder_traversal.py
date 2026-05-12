# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 005 -- Binary Tree Inorder Traversal
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 3
# =============================================================
#
# QUESTION:
#   Given the root of a binary tree, return the inorder (Left, Root, Right)
#   traversal of its nodes' values.
#
#   Example:
#     Input : root = [1,null,2,3]
#     Output: [1, 3, 2]
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def inorderTraversal(self, root):
        out, stack, cur = [], [], root
        while cur or stack:
            while cur: stack.append(cur); cur = cur.left
            cur = stack.pop(); out.append(cur.val); cur = cur.right
        return out

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(Solution().inorderTraversal(root))  # [1, 3, 2]
