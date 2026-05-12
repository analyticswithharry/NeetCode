# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 138 -- Matchsticks to Square
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 69
# =============================================================
#
# QUESTION:
#   Use all matchsticks to form a square. Return true if possible.
# =============================================================
def square(m):
    s=sum(m)
    if s%4: return False
    side=s//4; m.sort(reverse=True)
    if m[0]>side: return False
    sides=[0]*4
    def rec(i):
        if i==len(m): return sides[0]==sides[1]==sides[2]==side
        for j in range(4):
            if sides[j]+m[i]<=side:
                if j>0 and sides[j]==sides[j-1]: continue
                sides[j]+=m[i]
                if rec(i+1): return True
                sides[j]-=m[i]
        return False
    return rec(0)

if __name__=="__main__":
    print(square([1,1,2,2,2]))
    print(square([3,3,3,3,4]))
