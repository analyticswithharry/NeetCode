# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 215 -- Merge Triplets to Form Target Triplet
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 108
# =============================================================
#
# QUESTION:
#   Pick triplets where every value <= target; check if max across them equals target.
# =============================================================
mergeTriplets <- function(t,T){ g<-c(0,0,0); for(x in t){ if(all(x<=T)) g<-pmax(g,x) }; all(g==T) }
cat(mergeTriplets(list(c(2,5,3),c(1,8,4),c(1,7,5)),c(2,7,5)),"\n")
