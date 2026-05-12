# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 248 -- Detect Squares
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 124
# =============================================================
#
# QUESTION:
#   Add point or count axis-aligned squares with given query point.
# =============================================================
class DS:
    def __init__(s): s.c={}
    def add(s,p): s.c[tuple(p)]=s.c.get(tuple(p),0)+1
    def count(s,p):
        x,y=p; tot=0
        for (a,b),v in list(s.c.items()):
            if a==x or abs(a-x)!=abs(b-y): continue
            tot += v*s.c.get((a,y),0)*s.c.get((x,b),0)
        return tot
if __name__=="__main__":
    d=DS(); [d.add(p) for p in [[3,10],[11,2],[3,2]]]; print(d.count([11,10]))
