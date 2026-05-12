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

buildTree <- function(preorder, inorder){
    if (length(preorder) == 0) return(NULL)
    v <- preorder[1]; m <- which(inorder == v)
    list(val = v,
         left = buildTree(preorder[seq_len(m-1)+1], inorder[seq_len(m-1)]),
         right = buildTree(preorder[(m+1):length(preorder)], inorder[(m+1):length(inorder)]))
}
pre <- function(n) if (is.null(n)) c() else c(n$val, pre(n$left), pre(n$right))
t <- buildTree(c(3,9,20,15,7), c(9,3,15,20,7))
print(pre(t))
