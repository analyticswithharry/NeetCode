# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 079 -- Subtree of Another Tree
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 40
# =============================================================
#
# QUESTION:
#   Given roots of two trees root and subRoot, return true if subRoot is a subtree of root.
# =============================================================

same <- function(p,q){ if (is.null(p) && is.null(q)) return(TRUE); if (is.null(p)||is.null(q)||p$val!=q$val) return(FALSE); same(p$left,q$left) && same(p$right,q$right) }
isSubtree <- function(r, s){ if (is.null(r)) return(FALSE); if (same(r,s)) return(TRUE); isSubtree(r$left,s) || isSubtree(r$right,s) }
mk <- function(v,l=NULL,rr=NULL) list(val=v,left=l,right=rr)
r <- mk(3, mk(4, mk(1), mk(2)), mk(5))
s <- mk(4, mk(1), mk(2))
print(isSubtree(r, s))
