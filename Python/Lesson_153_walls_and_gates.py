# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 153 -- Walls And Gates
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 77
# =============================================================
#
# QUESTION:
#   Grid: -1 wall, 0 gate, INF empty. Fill each empty with distance to nearest gate.
# =============================================================
from collections import deque
INF=2**31-1
def walls(g):
    if not g: return g
    m,n=len(g),len(g[0]); q=deque()
    for i in range(m):
        for j in range(n):
            if g[i][j]==0: q.append((i,j))
    while q:
        i,j=q.popleft()
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj=i+di,j+dj
            if 0<=ni<m and 0<=nj<n and g[ni][nj]==INF:
                g[ni][nj]=g[i][j]+1; q.append((ni,nj))
    return g

if __name__=="__main__":
    g=[[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
    print(walls(g))
