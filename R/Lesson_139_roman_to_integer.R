# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 139 -- Roman to Integer
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 70
# =============================================================
#
# QUESTION:
#   Convert Roman numeral string to integer.
# =============================================================
r2i <- function(s){ m<-c(I=1,V=5,X=10,L=50,C=100,D=500,M=1000); cs<-rev(strsplit(s,"")[[1]]); t<-0; p<-0; for(c in cs){ v<-m[[c]]; if(v<p) t<-t-v else { t<-t+v; p<-v } }; t }
cat(r2i("III"),"\n"); cat(r2i("LVIII"),"\n"); cat(r2i("MCMXCIV"),"\n")
