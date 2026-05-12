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

inorder <- function(n){ if (is.null(n)) return(c()); c(inorder(n$left), n$val, inorder(n$right)) }
kthSmallest <- function(root, k) inorder(root)[k]
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
r <- mk(3, mk(1, NULL, mk(2)), mk(4))
print(kthSmallest(r, 1)); print(kthSmallest(r, 3))
