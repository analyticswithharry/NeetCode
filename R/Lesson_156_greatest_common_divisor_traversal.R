# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 156 -- Greatest Common Divisor Traversal
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 78
# =============================================================
#
# QUESTION:
#   You can move between indices i,j if gcd(nums[i],nums[j])>1. Return true iff every pair is connected.
# =============================================================
par <- NULL
f <- function(x){ while(par[x]!=x){ par[x]<<-par[par[x]]; x<-par[x] }; x }
u <- function(x,y){ x<-f(x); y<-f(y); if(x!=y) par[x]<<-y }
primes <- function(x){ r<-c(); d<-2; while(d*d<=x){ if(x%%d==0){ r<-c(r,d); while(x%%d==0) x<-x%/%d }; d<-d+1 }; if(x>1) r<-c(r,x); r }
can <- function(a){ n<-length(a); par<<-1:n; pm<-list(); for(i in 1:n) for(p in primes(a[i])){ k<-as.character(p); if(!is.null(pm[[k]])) u(i,pm[[k]]) else pm[[k]]<-i }; r<-f(1); all(sapply(1:n,f)==r) }
cat(can(c(2,3,6)),"\n"); cat(can(c(3,9,5)),"\n"); cat(can(c(4,3,12,8)),"\n")
