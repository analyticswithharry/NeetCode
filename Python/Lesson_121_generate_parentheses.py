# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 121 -- Generate Parentheses
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 61
# =============================================================
#
# QUESTION:
#   Given n pairs of parentheses, generate all combinations of well-formed parentheses.
# =============================================================
def gen(n):
    res=[]
    def rec(s,o,c):
        if len(s)==2*n: res.append(s); return
        if o<n: rec(s+"(",o+1,c)
        if c<o: rec(s+")",o,c+1)
    rec("",0,0); return res

if __name__=="__main__":
    print(gen(3))
