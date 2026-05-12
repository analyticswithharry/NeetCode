# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 218 -- Minimum Height Trees
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 109
# =============================================================
#
# QUESTION:
#   Given an undirected tree, find roots that produce minimum-height trees (peel leaves BFS).
# =============================================================
from collections import deque
def findMHT(n,edges):
    if n==1: return [0]
    g=[set() for _ in range(n)]; deg=[0]*n
    for a,b in edges: g[a].add(b); g[b].add(a); deg[a]+=1; deg[b]+=1
    q=deque(i for i in range(n) if deg[i]==1); rem=n
    while rem>2:
        sz=len(q); rem-=sz
        for _ in range(sz):
            x=q.popleft()
            for y in g[x]:
                deg[y]-=1
                if deg[y]==1: q.append(y)
    return list(q)
if __name__=="__main__":
    print(findMHT(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))
