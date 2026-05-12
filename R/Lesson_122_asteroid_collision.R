# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 122 -- Asteroid Collision
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 61
# =============================================================
#
# QUESTION:
#   Given an array of asteroids (positive=right, negative=left), return state after all collisions.
# =============================================================
collide <- function(a){ st<-c(); for(x in a){ alive<-TRUE; while(alive && length(st)>0 && x<0 && st[length(st)]>0){ if(st[length(st)] < -x){ st<-st[-length(st)] } else if(st[length(st)] == -x){ st<-st[-length(st)]; alive<-FALSE } else alive<-FALSE }; if(alive) st<-c(st,x) }; st }
print(collide(c(5,10,-5))); print(collide(c(8,-8))); print(collide(c(10,2,-5)))
