# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 217 -- Evaluate Division
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 109
# =============================================================
#
# QUESTION:
#   Given equations a/b=value, answer queries x/y. Build weighted graph and DFS.
# =============================================================
from collections import defaultdict
def calcEquation(eq,vals,q):
    g=defaultdict(dict)
    for (a,b),v in zip(eq,vals): g[a][b]=v; g[b][a]=1/v
    def dfs(s,t,seen):
        if s not in g or t not in g: return -1.0
        if s==t: return 1.0
        seen.add(s)
        for n,w in g[s].items():
            if n in seen: continue
            r=dfs(n,t,seen)
            if r!=-1.0: return w*r
        return -1.0
    return [dfs(a,b,set()) for a,b in q]
if __name__=="__main__":
    print(calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"]]))
