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

preorderTraversal <- function(node) {
    if (is.null(node)) return(integer(0))
    c(node$val, preorderTraversal(node$left), preorderTraversal(node$right))
}

root <- list(val=1, left=NULL, right=list(val=2, left=list(val=3, left=NULL, right=NULL), right=NULL))
print(preorderTraversal(root))  # 1 2 3
