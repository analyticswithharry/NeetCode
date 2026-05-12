# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 132 -- Split Array Largest Sum
# Category   : Binary Search
# Difficulty : Hard
# Study Plan : Day 66
# =============================================================
#
# QUESTION:
#   Split nums into k non-empty contiguous parts to minimize the largest sum among parts.
# =============================================================
def split(a,k):
    def can(mx):
        c,s=1,0
        for x in a:
            if s+x>mx: c+=1; s=x
            else: s+=x
        return c<=k
    lo,hi=max(a),sum(a)
    while lo<hi:
        m=(lo+hi)//2
        if can(m): hi=m
        else: lo=m+1
    return lo

if __name__=="__main__":
    print(split([7,2,5,10,8],2))
