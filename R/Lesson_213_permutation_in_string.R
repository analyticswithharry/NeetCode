# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 213 -- Permutation in String
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 107
# =============================================================
#
# QUESTION:
#   Return true if s2 contains a permutation of s1.
# =============================================================
checkInclusion <- function(s1,s2){ if(nchar(s1)>nchar(s2)) return(FALSE); a<-table(factor(strsplit(s1,"")[[1]],levels=letters)); v<-strsplit(s2,"")[[1]]; for(i in seq_along(v)){ if(i==1){ b<-table(factor(v[1:nchar(s1)],levels=letters)); if(all(a==b)) return(TRUE) } else if(i+nchar(s1)-1<=length(v)){ b<-table(factor(v[i:(i+nchar(s1)-1)],levels=letters)); if(all(a==b)) return(TRUE) } }; FALSE }
cat(checkInclusion("ab","eidbaooo"),"\n")
