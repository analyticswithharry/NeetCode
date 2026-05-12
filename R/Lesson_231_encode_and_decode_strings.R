# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 231 -- Encode and Decode Strings
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 116
# =============================================================
#
# QUESTION:
#   Length-prefix encoding for arbitrary strings.
# =============================================================
encode <- function(a) paste0(sapply(a,function(s) paste0(nchar(s),"#",s)),collapse="")
decode <- function(s){ r<-c(); i<-1; while(i<=nchar(s)){ j<-i+regexpr("#",substr(s,i,nchar(s)))-1; n<-as.integer(substr(s,i,j-1)); r<-c(r,substr(s,j+1,j+n)); i<-j+1+n }; r }
cat(encode(c("hello","world")),"\n"); print(decode(encode(c("hello","world"))))
