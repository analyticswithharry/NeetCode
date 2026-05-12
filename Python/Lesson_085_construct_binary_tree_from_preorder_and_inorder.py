# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 085 -- Construct Binary Tree from Preorder and Inorder
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 43
# =============================================================
#
# QUESTION:
#   Given preorder and inorder traversals of a binary tree (no duplicates), construct and return the tree.
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def buildTree(self, preorder, inorder):
        idx = {v:i for i,v in enumerate(inorder)}
        self.p = 0
        def go(l, r):
            if l > r: return None
            v = preorder[self.p]; self.p += 1
            root = TreeNode(v); m = idx[v]
            root.left = go(l, m-1); root.right = go(m+1, r)
            return root
        return go(0, len(inorder)-1)

def pre(n):
    if not n: return []
    return [n.val] + pre(n.left) + pre(n.right)

if __name__ == "__main__":
    t = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(pre(t))
