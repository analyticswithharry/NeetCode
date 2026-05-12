# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 155 -- Build a Matrix With Conditions
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 78
# =============================================================
#
# QUESTION:
#   Given k rows/cols and conditions for row/col orderings, place 1..k so each appears once and conditions are satisfied. Return matrix or [].
# =============================================================
from collections import defaultdict, deque
def topo(k, conds):
    adj=defaultdict(list); ind=[0]*(k+1)
    for a,b in conds:
        adj[a].append(b); ind[b]+=1
    q=deque([i for i in range(1,k+1) if ind[i]==0]); o=[]
    while q:
        x=q.popleft(); o.append(x)
        for y in adj[x]:
            ind[y]-=1
            if ind[y]==0: q.append(y)
    return o if len(o)==k else []
def build(k, rowC, colC):
    r=topo(k,rowC); c=topo(k,colC)
    if not r or not c: return []
    pos={v:i for i,v in enumerate(c)}
    g=[[0]*k for _ in range(k)]
    for i,v in enumerate(r): g[i][pos[v]]=v
    return g

if __name__=="__main__":
    print(build(3,[[1,2],[3,2]],[[2,1],[3,2]]))
