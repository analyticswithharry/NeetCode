# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 249 -- Serialize And Deserialize Binary Tree
# Category   : Trees
# Difficulty : Hard
# Study Plan : Day 125
# =============================================================
#
# QUESTION:
#   Pre-order serialize with null markers; queue-based deserialize.
# =============================================================
class T:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def ser(r):
    out=[]
    def dfs(n):
        if not n: out.append("#"); return
        out.append(str(n.v)); dfs(n.l); dfs(n.r)
    dfs(r); return ",".join(out)
def des(s):
    it=iter(s.split(","))
    def dfs():
        x=next(it)
        if x=="#": return None
        n=T(int(x)); n.l=dfs(); n.r=dfs(); return n
    return dfs()
if __name__=="__main__":
    r=T(1,T(2),T(3,T(4),T(5))); s=ser(r); print(s); print(ser(des(s)))
