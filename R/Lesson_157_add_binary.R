# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 157 -- Add Binary
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 79
# =============================================================
#
# QUESTION:
#   Given two binary strings, return their sum as a binary string.
# =============================================================
addBin <- function(a,b){ i<-nchar(a); j<-nchar(b); c<-0; r<-c(); while(i>=1 || j>=1 || c>0){ s<-c; if(i>=1){ s<-s+as.integer(substr(a,i,i)); i<-i-1 }; if(j>=1){ s<-s+as.integer(substr(b,j,j)); j<-j-1 }; r<-c(s%%2,r); c<-s%/%2 }; paste(r,collapse="") }
cat(addBin("11","1"),"\n"); cat(addBin("1010","1011"),"\n")
