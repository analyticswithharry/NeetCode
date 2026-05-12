# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 078 -- Same Tree
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 39
# =============================================================
#
# QUESTION:
#   Given two binary trees, check if they are structurally identical with same node values.
# =============================================================

# Represent a tree as a nested list: list(val, left, right) or NULL
isSameTree <- function(p, q){
    if (is.null(p) && is.null(q)) return(TRUE)
    if (is.null(p) || is.null(q) || p$val != q$val) return(FALSE)
    isSameTree(p$left, q$left) && isSameTree(p$right, q$right)
}
a <- list(val=1, left=list(val=2,left=NULL,right=NULL), right=list(val=3,left=NULL,right=NULL))
b <- list(val=1, left=list(val=2,left=NULL,right=NULL), right=list(val=3,left=NULL,right=NULL))
print(isSameTree(a,b))
