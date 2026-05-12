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

isValidBST <- function(root){
    go <- function(n, lo, hi){ if (is.null(n)) return(TRUE)
        if (n$val <= lo || n$val >= hi) return(FALSE)
        go(n$left, lo, n$val) && go(n$right, n$val, hi) }
    go(root, -Inf, Inf)
}
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
print(isValidBST(mk(2, mk(1), mk(3))))
print(isValidBST(mk(5, mk(1), mk(4, mk(3), mk(6)))))
