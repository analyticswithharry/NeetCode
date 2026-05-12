# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 074 -- LRU Cache
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 37
# =============================================================
#
# QUESTION:
#   Design an LRU cache with O(1) get and put.
# =============================================================

# Simple LRU using a named list with manual recency list
LRU <- function(cap){
    e <- new.env(); e$cap <- cap; e$keys <- c(); e$vals <- list()
    e$get <- function(k){
        if (!(k %in% e$keys)) return(-1)
        v <- e$vals[[as.character(k)]]; e$keys <- c(setdiff(e$keys, k), k); v
    }
    e$put <- function(k, v){
        e$vals[[as.character(k)]] <- v
        e$keys <- c(setdiff(e$keys, k), k)
        if (length(e$keys) > e$cap){
            old <- e$keys[1]; e$keys <- e$keys[-1]; e$vals[[as.character(old)]] <- NULL
        }
    }
    e
}
c <- LRU(2); c$put(1,1); c$put(2,2); print(c$get(1))
c$put(3,3); print(c$get(2)); c$put(4,4); print(c(c$get(1), c$get(3), c$get(4)))
