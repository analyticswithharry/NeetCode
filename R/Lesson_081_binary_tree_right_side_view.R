# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 081 -- Binary Tree Right Side View
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 41
# =============================================================
#
# QUESTION:
#   Return the values of nodes you'd see ordered from top to bottom from the right side.
#
#   Example: [1,2,3,null,5,null,4] -> [1,3,4]
# =============================================================

rightSideView <- function(root){
    if (is.null(root)) return(c())
    out <- c(); q <- list(root)
    while (length(q) > 0){
        nq <- list(); n <- length(q)
        for (i in seq_along(q)){ x <- q[[i]]; if (i == n) out <- c(out, x$val)
            if (!is.null(x$left)) nq <- c(nq, list(x$left))
            if (!is.null(x$right)) nq <- c(nq, list(x$right)) }
        q <- nq
    }
    out
}
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
print(rightSideView(mk(1, mk(2, NULL, mk(5)), mk(3, NULL, mk(4)))))
