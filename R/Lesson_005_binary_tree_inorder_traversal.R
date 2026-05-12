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

# Tree as nested list: list(val, left, right). NULL for missing children.
inorderTraversal <- function(node) {
    if (is.null(node)) return(integer(0))
    c(inorderTraversal(node$left), node$val, inorderTraversal(node$right))
}

root <- list(val=1, left=NULL, right=list(val=2, left=list(val=3, left=NULL, right=NULL), right=NULL))
print(inorderTraversal(root))  # 1 3 2
