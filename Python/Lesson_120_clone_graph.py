# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 120 -- Clone Graph
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 60
# =============================================================
#
# QUESTION:
#   Given a node in a connected undirected graph, return a deep copy of the graph.
# =============================================================
class Node:
    def __init__(self,v,nei=None): self.val=v; self.neighbors=nei or []

def clone(n):
    if not n: return None
    seen={}
    def dfs(x):
        if x in seen: return seen[x]
        c=Node(x.val); seen[x]=c
        for y in x.neighbors: c.neighbors.append(dfs(y))
        return c
    return dfs(n)

if __name__=="__main__":
    a=Node(1); b=Node(2); a.neighbors=[b]; b.neighbors=[a]
    c=clone(a); print(c.val, c.neighbors[0].val, c.neighbors[0].neighbors[0].val)
