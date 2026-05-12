# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 063 -- Encode and Decode Strings
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 32
# =============================================================
#
# QUESTION:
#   Design encode/decode of a list of strings into one string and back.
#
#   Strategy: prefix each string with its length and a delimiter (e.g., 5#hello).
# =============================================================

encode <- function(strs) paste0(sapply(strs, function(s) paste0(nchar(s),"#",s)), collapse="")
decode <- function(s){ out <- c(); i <- 1
    while (i <= nchar(s)){ j <- regexpr("#", substr(s,i,nchar(s)))[1] + i - 1
        n <- as.integer(substr(s,i,j-1)); out <- c(out, substr(s,j+1,j+n)); i <- j+1+n }
    out
}
e <- encode(c("lint","code","love","you")); print(e); print(decode(e))
