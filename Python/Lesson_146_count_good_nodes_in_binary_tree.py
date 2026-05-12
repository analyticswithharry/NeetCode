# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 146 -- Count Good Nodes In Binary Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 73
# =============================================================
#
# QUESTION:
#   A node is good if no node on the root-to-node path has a value greater. Count good nodes.
# =============================================================
class TN:
    def __init__(self,v,l=None,r=None): self.val=v; self.left=l; self.right=r
def good(root):
    def rec(n,m):
        if not n: return 0
        c=1 if n.val>=m else 0
        m=max(m,n.val)
        return c+rec(n.left,m)+rec(n.right,m)
    return rec(root,float('-inf'))

if __name__=="__main__":
    r=TN(3,TN(1,TN(3)),TN(4,TN(1),TN(5)))
    print(good(r))
