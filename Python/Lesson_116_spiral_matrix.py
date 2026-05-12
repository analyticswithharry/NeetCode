# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 116 -- Spiral Matrix
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 58
# =============================================================
#
# QUESTION:
#   Given m x n matrix, return all elements in spiral order.
# =============================================================
def spiral(m):
    res=[]
    if not m: return res
    t,b,l,r=0,len(m)-1,0,len(m[0])-1
    while t<=b and l<=r:
        for j in range(l,r+1): res.append(m[t][j])
        t+=1
        for i in range(t,b+1): res.append(m[i][r])
        r-=1
        if t<=b:
            for j in range(r,l-1,-1): res.append(m[b][j])
            b-=1
        if l<=r:
            for i in range(b,t-1,-1): res.append(m[i][l])
            l+=1
    return res

if __name__=="__main__":
    print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
