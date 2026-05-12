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

goodNodes <- function(root){
    dfs <- function(n, mx){ if (is.null(n)) return(0)
        c <- if (n$val >= mx) 1 else 0
        m <- max(mx, n$val)
        c + dfs(n$left, m) + dfs(n$right, m) }
    dfs(root, root$val)
}
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
print(goodNodes(mk(3, mk(1, mk(3)), mk(4, mk(1), mk(5)))))
