// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 140 -- Set Matrix Zeroes
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 70
// =============================================================
//
// QUESTION:
//   Given m x n matrix, if an element is 0, set its entire row and column to 0. In place.
// =============================================================
function setZero(g){const m=g.length,n=g[0].length;let r0=false,c0=false;for(let j=0;j<n;j++)if(g[0][j]===0)r0=true;for(let i=0;i<m;i++)if(g[i][0]===0)c0=true;for(let i=1;i<m;i++)for(let j=1;j<n;j++)if(g[i][j]===0){g[i][0]=0;g[0][j]=0;}for(let i=1;i<m;i++)for(let j=1;j<n;j++)if(g[i][0]===0||g[0][j]===0)g[i][j]=0;if(r0)for(let j=0;j<n;j++)g[0][j]=0;if(c0)for(let i=0;i<m;i++)g[i][0]=0;return g;}
console.log(setZero([[1,1,1],[1,0,1],[1,1,1]]));
