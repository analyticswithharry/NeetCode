# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 112 -- Sum of Two Integers
# Category   : Bit Manipulation
# Difficulty : Medium
# Study Plan : Day 56
# =============================================================
#
# QUESTION:
#   Given two integers a and b, return the sum without using + or -.
# =============================================================
add <- function(a,b){ while(b!=0){ c <- bitwShiftL(bitwAnd(a,b),1); a <- bitwXor(a,b); b <- c }; a }
cat(add(1,2),"\n"); cat(add(-2,3),"\n")
