# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 143 -- Palindromic Substrings
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 72
# =============================================================
#
# QUESTION:
#   Count number of palindromic substrings in s.
# =============================================================
count <- function(s){ n<-nchar(s); c<-0; ex<-function(a,b){ while(a>=1 && b<=n && substr(s,a,a)==substr(s,b,b)){ c<<-c+1; a<-a-1; b<-b+1 } }; for(i in 1:n){ ex(i,i); ex(i,i+1) }; c }
cat(count("abc"),"\n"); cat(count("aaa"),"\n")
