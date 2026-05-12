# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 123 -- Design HashSet
# Category   : Arrays and Hashing
# Difficulty : Easy
# Study Plan : Day 62
# =============================================================
#
# QUESTION:
#   Design a HashSet (without built-in set): add, remove, contains.
# =============================================================
MyHashSet <- function(){ env <- new.env(hash=TRUE); list(add=function(k) assign(as.character(k),TRUE,envir=env), remove=function(k){ if(exists(as.character(k),envir=env)) rm(list=as.character(k),envir=env) }, contains=function(k) exists(as.character(k),envir=env)) }
s <- MyHashSet(); s$add(1); s$add(2); cat(s$contains(1), s$contains(3),"\n"); s$remove(2); cat(s$contains(2),"\n")
