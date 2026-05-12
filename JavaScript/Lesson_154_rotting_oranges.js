// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 154 -- Rotting Oranges
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 77
// =============================================================
//
// QUESTION:
//   0 empty, 1 fresh, 2 rotten. Each minute rotten infects 4-neighbor fresh. Min minutes to rot all, or -1.
// =============================================================
function rot(g){const m=g.length,n=g[0].length;const q=[];let fresh=0;for(let i=0;i<m;i++)for(let j=0;j<n;j++){if(g[i][j]===2)q.push([i,j,0]);else if(g[i][j]===1)fresh++;}let t=0;while(q.length){const [i,j,k]=q.shift();t=k;for(const [di,dj] of [[-1,0],[1,0],[0,-1],[0,1]]){const ni=i+di,nj=j+dj;if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]===1){g[ni][nj]=2;fresh--;q.push([ni,nj,k+1]);}}}return fresh?-1:t;}
console.log(rot([[2,1,1],[1,1,0],[0,1,1]]));console.log(rot([[2,1,1],[0,1,1],[1,0,1]]));
