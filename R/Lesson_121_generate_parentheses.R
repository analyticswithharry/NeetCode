# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 121 -- Generate Parentheses
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 61
# =============================================================
#
# QUESTION:
#   Given n pairs of parentheses, generate all combinations of well-formed parentheses.
# =============================================================
gen <- function(n){ r<-c(); rec <- function(s,o,c){ if(nchar(s)==2*n){ r[[length(r)+1]]<<-s; return() }; if(o<n) rec(paste0(s,"("),o+1,c); if(c<o) rec(paste0(s,")"),o,c+1) }; rec("",0,0); r }
print(gen(3))
