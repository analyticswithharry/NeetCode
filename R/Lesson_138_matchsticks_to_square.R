# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 138 -- Matchsticks to Square
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 69
# =============================================================
#
# QUESTION:
#   Use all matchsticks to form a square. Return true if possible.
# =============================================================
square <- function(m){ s<-sum(m); if(s%%4!=0) return(FALSE); side<-s/4; m<-sort(m,decreasing=TRUE); if(m[1]>side) return(FALSE); sides<-c(0,0,0,0); rec<-function(i){ if(i>length(m)) return(sides[1]==side && sides[2]==side && sides[3]==side); for(j in 1:4){ if(sides[j]+m[i]>side) next; if(j>1 && sides[j]==sides[j-1]) next; sides[j]<<-sides[j]+m[i]; if(rec(i+1)) return(TRUE); sides[j]<<-sides[j]-m[i] }; FALSE }; rec(1) }
cat(square(c(1,1,2,2,2)),"\n"); cat(square(c(3,3,3,3,4)),"\n")
