# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 158 -- Minimum Array End
# Category   : Bit Manipulation
# Difficulty : Medium
# Study Plan : Day 79
# =============================================================
#
# QUESTION:
#   Given n and x, return min possible value v such that AND of n distinct integers (>=x, <=v, all sharing bits of x) equals x. Equivalent: spread (n-1) over the zero-bits of x.
# =============================================================
minEnd <- function(n,x){ n<-n-1; r<-x; bit<-1; nb<-1; while(nb<=n){ if(bitwAnd(x,bit)==0){ if(bitwAnd(n,nb)!=0) r<-bitwOr(r,bit); nb<-bitwShiftL(nb,1) }; bit<-bitwShiftL(bit,1) }; r }
cat(minEnd(3,4),"\n"); cat(minEnd(2,7),"\n")
