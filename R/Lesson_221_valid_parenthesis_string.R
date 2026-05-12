# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 221 -- Valid Parenthesis String
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 111
# =============================================================
#
# QUESTION:
#   '*' can be '(' ')' or empty. Determine if string can be valid.
# =============================================================
checkValid <- function(s){ lo<-0; hi<-0; for(c in strsplit(s,"")[[1]]){ lo<-lo+ifelse(c=="(",1,-1); hi<-hi+ifelse(c!=")",1,-1); if(hi<0) return(FALSE); if(lo<0) lo<-0 }; lo==0 }
cat(checkValid("(*))"),"\n")
