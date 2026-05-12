# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 120 -- Clone Graph
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 60
# =============================================================
#
# QUESTION:
#   Given a node in a connected undirected graph, return a deep copy of the graph.
# =============================================================
# Simulate clone via id refs
clone <- function(adj){ adj } # adjacency-list copy is the deep-copy in R
adj <- list(`1`=c(2), `2`=c(1)); print(clone(adj))
