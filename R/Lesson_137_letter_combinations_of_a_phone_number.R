# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 137 -- Letter Combinations of a Phone Number
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 69
# =============================================================
#
# QUESTION:
#   Given digits 2-9, return all possible letter combinations the number could represent.
# =============================================================
letters_pn <- function(d){ if(nchar(d)==0) return(c()); m<-list("2"="abc","3"="def","4"="ghi","5"="jkl","6"="mno","7"="pqrs","8"="tuv","9"="wxyz"); r<-c(""); for(c in strsplit(d,"")[[1]]){ n<-c(); for(p in r) for(x in strsplit(m[[c]],"")[[1]]) n<-c(n,paste0(p,x)); r<-n }; r }
print(letters_pn("23"))
