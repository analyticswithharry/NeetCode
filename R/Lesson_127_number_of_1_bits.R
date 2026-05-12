# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 127 -- Number of 1 Bits
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 64
# =============================================================
#
# QUESTION:
#   Return the number of 1 bits in unsigned int.
# =============================================================
hw <- function(n){ c<-0; while(n!=0){ if(bitwAnd(n,1)==1) c<-c+1; n<-bitwShiftR(n,1) }; c }
cat(hw(11),"\n"); cat(hw(128),"\n")
