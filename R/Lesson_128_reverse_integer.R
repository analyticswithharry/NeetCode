# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 128 -- Reverse Integer
# Category   : Bit Manipulation
# Difficulty : Medium
# Study Plan : Day 64
# =============================================================
#
# QUESTION:
#   Reverse digits of a signed 32-bit integer; return 0 on overflow.
# =============================================================
rev <- function(x){ s<-sign(x); x<-abs(x); r<-0; while(x>0){ r<-r*10+x%%10; x<-x%/%10 }; r<-r*s; if(r < -2^31 || r > 2^31-1) 0 else r }
cat(rev(123),"\n"); cat(rev(-456),"\n"); cat(rev(1534236469),"\n")
