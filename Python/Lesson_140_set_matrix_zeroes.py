# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 140 -- Set Matrix Zeroes
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 70
# =============================================================
#
# QUESTION:
#   Given m x n matrix, if an element is 0, set its entire row and column to 0. In place.
# =============================================================
def setZero(g):
    m,n=len(g),len(g[0]); r0=any(g[0][j]==0 for j in range(n)); c0=any(g[i][0]==0 for i in range(m))
    for i in range(1,m):
        for j in range(1,n):
            if g[i][j]==0: g[i][0]=0; g[0][j]=0
    for i in range(1,m):
        for j in range(1,n):
            if g[i][0]==0 or g[0][j]==0: g[i][j]=0
    if r0:
        for j in range(n): g[0][j]=0
    if c0:
        for i in range(m): g[i][0]=0
    return g

if __name__=="__main__":
    print(setZero([[1,1,1],[1,0,1],[1,1,1]]))
