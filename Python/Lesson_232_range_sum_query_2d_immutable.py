# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 232 -- Range Sum Query 2D Immutable
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 116
# =============================================================
#
# QUESTION:
#   Build prefix sum 2D for O(1) region queries.
# =============================================================
class NM:
    def __init__(s,m):
        if not m: s.p=[]; return
        R,C=len(m),len(m[0])
        s.p=[[0]*(C+1) for _ in range(R+1)]
        for i in range(R):
            for j in range(C):
                s.p[i+1][j+1]=m[i][j]+s.p[i][j+1]+s.p[i+1][j]-s.p[i][j]
    def sumRegion(s,r1,c1,r2,c2):
        return s.p[r2+1][c2+1]-s.p[r1][c2+1]-s.p[r2+1][c1]+s.p[r1][c1]
if __name__=="__main__":
    n=NM([[3,0,1],[5,6,3],[1,2,0]]); print(n.sumRegion(0,0,2,2)); print(n.sumRegion(1,1,2,2))
