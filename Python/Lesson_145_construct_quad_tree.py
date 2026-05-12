# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 145 -- Construct Quad Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 73
# =============================================================
#
# QUESTION:
#   Given an n x n grid of 0/1, build a quad tree representation. Return root.
# =============================================================
class QN:
    def __init__(self,v,leaf,tl=None,tr=None,bl=None,br=None):
        self.val=v; self.isLeaf=leaf; self.tl=tl; self.tr=tr; self.bl=bl; self.br=br
def build(g):
    def rec(r,c,n):
        if all(g[i][j]==g[r][c] for i in range(r,r+n) for j in range(c,c+n)):
            return QN(g[r][c]==1,True)
        h=n//2
        return QN(True,False,rec(r,c,h),rec(r,c+h,h),rec(r+h,c,h),rec(r+h,c+h,h))
    return rec(0,0,len(g))

def serialize(n):
    if n.isLeaf: return [int(n.val)]
    return ['#']+serialize(n.tl)+serialize(n.tr)+serialize(n.bl)+serialize(n.br)

if __name__=="__main__":
    g=[[0,1],[1,0]]
    print(serialize(build(g)))
