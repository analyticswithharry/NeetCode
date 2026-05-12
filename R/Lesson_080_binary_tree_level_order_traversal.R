# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 080 -- Binary Tree Level Order Traversal
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 40
# =============================================================
#
# QUESTION:
#   Return level-order traversal of a binary tree as list of lists.
#
#   Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
# =============================================================

levelOrder <- function(root){
    if (is.null(root)) return(list())
    out <- list(); q <- list(root)
    while (length(q) > 0){
        lvl <- c(); nq <- list()
        for (n in q){ lvl <- c(lvl, n$val)
            if (!is.null(n$left)) nq <- c(nq, list(n$left))
            if (!is.null(n$right)) nq <- c(nq, list(n$right)) }
        out <- c(out, list(lvl)); q <- nq
    }
    out
}
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
print(levelOrder(mk(3, mk(9), mk(20, mk(15), mk(7)))))
