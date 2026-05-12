# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 150 -- Online Stock Span
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 75
# =============================================================
#
# QUESTION:
#   Implement StockSpanner.next(price): consecutive days <= today's price (including today).
# =============================================================
class StockSpanner:
    def __init__(self): self.st=[]
    def next(self,p):
        s=1
        while self.st and self.st[-1][0]<=p: _,k=self.st.pop(); s+=k
        self.st.append((p,s)); return s

if __name__=="__main__":
    s=StockSpanner()
    print([s.next(x) for x in [100,80,60,70,60,75,85]])
