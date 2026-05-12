# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 072 -- Linked List Cycle
# Category   : Linked List
# Difficulty : Easy
# Study Plan : Day 36
# =============================================================
#
# QUESTION:
#   Determine if a linked list has a cycle. Floyd's tortoise and hare.
# =============================================================

# R has no native pointer-based linked list; emulate cycle with index successor vector.
hasCycle <- function(next_idx, start=1){
    slow <- start; fast <- start
    repeat {
        if (is.na(next_idx[fast]) || is.na(next_idx[next_idx[fast]])) return(FALSE)
        slow <- next_idx[slow]; fast <- next_idx[next_idx[fast]]
        if (slow == fast) return(TRUE)
    }
}
print(hasCycle(c(2,3,1)))   # 1->2->3->1 cycle
print(hasCycle(c(2,NA)))    # 1->2->NA no cycle
