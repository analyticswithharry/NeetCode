# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 215 -- Merge Triplets to Form Target Triplet
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 108
# =============================================================
#
# QUESTION:
#   Pick triplets where every value <= target; check if max across them equals target.
# =============================================================
def mergeTriplets(t,T):
    g=[0,0,0]
    for x in t:
        if x[0]<=T[0] and x[1]<=T[1] and x[2]<=T[2]:
            g=[max(g[i],x[i]) for i in range(3)]
    return g==T
if __name__=="__main__":
    print(mergeTriplets([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]))
