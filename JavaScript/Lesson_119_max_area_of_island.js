// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 119 -- Max Area of Island
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 60
// =============================================================
//
// QUESTION:
//   Given m x n binary grid, return max area of an island (4-directionally connected 1s).
// =============================================================
function maxArea(g){const m=g.length,n=g[0].length;let best=0;function dfs(i,j){if(i<0||j<0||i>=m||j>=n||g[i][j]!==1)return 0;g[i][j]=0;return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1);}for(let i=0;i<m;i++)for(let j=0;j<n;j++)if(g[i][j]===1)best=Math.max(best,dfs(i,j));return best;}
console.log(maxArea([[1,1,0],[1,0,0],[0,0,1]]));
