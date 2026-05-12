# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 082 -- Count Good Nodes in Binary Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 41
# =============================================================
#
# QUESTION:
#   A node X is good if no node on the path from root to X has value greater than X. Count good nodes.
#
#   Example: [3,1,4,3,null,1,5] -> 4
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def goodNodes(self, root):
        def dfs(n, mx):
            if not n: return 0
            c = 1 if n.val >= mx else 0
            mx = max(mx, n.val)
            return c + dfs(n.left, mx) + dfs(n.right, mx)
        return dfs(root, root.val)

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print(Solution().goodNodes(r))
