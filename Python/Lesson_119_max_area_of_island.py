# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 119 -- Max Area of Island
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 60
# =============================================================
#
# QUESTION:
#   Given m x n binary grid, return max area of an island (4-directionally connected 1s).
# =============================================================
def maxArea(g):
    m,n=len(g),len(g[0]); best=0
    def dfs(i,j):
        if i<0 or j<0 or i>=m or j>=n or g[i][j]!=1: return 0
        g[i][j]=0
        return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
    for i in range(m):
        for j in range(n):
            if g[i][j]==1: best=max(best,dfs(i,j))
    return best

if __name__=="__main__":
    print(maxArea([[1,1,0],[1,0,0],[0,0,1]]))
