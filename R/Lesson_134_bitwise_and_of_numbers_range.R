# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 134 -- Bitwise AND of Numbers Range
# Category   : Bit Manipulation
# Difficulty : Medium
# Study Plan : Day 67
# =============================================================
#
# QUESTION:
#   Given range [m,n], return the bitwise AND of all numbers in this range, inclusive.
# =============================================================
rangeAnd <- function(m,n){ s<-0; while(m!=n){ m<-bitwShiftR(m,1); n<-bitwShiftR(n,1); s<-s+1 }; bitwShiftL(m,s) }
cat(rangeAnd(5,7),"\n"); cat(rangeAnd(0,0),"\n")
