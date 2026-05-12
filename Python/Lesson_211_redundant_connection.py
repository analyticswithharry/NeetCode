# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 211 -- Redundant Connection
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 106
# =============================================================
#
# QUESTION:
#   Given an n-node tree with one extra edge (forming exactly one cycle), return the edge that can be removed.
# =============================================================
def findRedundant(edges):
    p=list(range(len(edges)+1))
    def f(x):
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    for a,b in edges:
        ra,rb=f(a),f(b)
        if ra==rb: return [a,b]
        p[ra]=rb
if __name__=="__main__":
    print(findRedundant([[1,2],[1,3],[2,3]]))
    print(findRedundant([[1,2],[2,3],[3,4],[1,4],[1,5]]))
