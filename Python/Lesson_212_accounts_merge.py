# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 212 -- Accounts Merge
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 106
# =============================================================
#
# QUESTION:
#   Merge accounts that share any common email. Return merged accounts with name + sorted unique emails.
# =============================================================
def accountsMerge(acc):
    p={}
    def f(x):
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    own={}
    for a in acc:
        for e in a[1:]:
            p.setdefault(e,e); own[e]=a[0]
            p[f(e)]=f(a[1])
    g={}
    for e in p: g.setdefault(f(e),[]).append(e)
    return [[own[v[0]]]+sorted(v) for v in g.values()]
if __name__=="__main__":
    print(accountsMerge([["A","a@x","b@x"],["A","b@x","c@x"],["B","d@x"]]))
