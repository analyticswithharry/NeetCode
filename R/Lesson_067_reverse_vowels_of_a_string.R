# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 067 -- Reverse Vowels of a String
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 34
# =============================================================
#
# QUESTION:
#   Reverse only the vowels of a string. Vowels: a,e,i,o,u (and uppercase).
#
#   Example: hello -> holle
# =============================================================

reverseVowels <- function(s){
    v <- c("a","e","i","o","u","A","E","I","O","U")
    a <- strsplit(s,"")[[1]]; l <- 1; r <- length(a)
    while (l<r){
        while (l<r && !(a[l] %in% v)) l <- l+1
        while (l<r && !(a[r] %in% v)) r <- r-1
        tmp <- a[l]; a[l] <- a[r]; a[r] <- tmp; l <- l+1; r <- r-1
    }
    paste(a, collapse="")
}
print(reverseVowels("hello")); print(reverseVowels("leetcode"))
