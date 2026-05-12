# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 115 -- Plus One
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 58
# =============================================================
#
# QUESTION:
#   Given a non-empty array of decimal digits representing a non-negative integer, add one and return the resulting array.
# =============================================================
plusOne <- function(d){ for(i in length(d):1){ if(d[i]<9){ d[i]<-d[i]+1; return(d) }; d[i]<-0 }; c(1,d) }
print(plusOne(c(1,2,3))); print(plusOne(c(9,9)))
