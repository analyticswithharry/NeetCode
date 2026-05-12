# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 154 -- Rotting Oranges
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 77
# =============================================================
#
# QUESTION:
#   0 empty, 1 fresh, 2 rotten. Each minute rotten infects 4-neighbor fresh. Min minutes to rot all, or -1.
# =============================================================
from collections import deque
def rot(g):
    m,n=len(g),len(g[0]); q=deque(); fresh=0
    for i in range(m):
        for j in range(n):
            if g[i][j]==2: q.append((i,j,0))
            elif g[i][j]==1: fresh+=1
    t=0
    while q:
        i,j,k=q.popleft(); t=k
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj=i+di,j+dj
            if 0<=ni<m and 0<=nj<n and g[ni][nj]==1:
                g[ni][nj]=2; fresh-=1; q.append((ni,nj,k+1))
    return -1 if fresh else t

if __name__=="__main__":
    print(rot([[2,1,1],[1,1,0],[0,1,1]]))
    print(rot([[2,1,1],[0,1,1],[1,0,1]]))
