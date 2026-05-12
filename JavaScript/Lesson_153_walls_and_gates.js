// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 153 -- Walls And Gates
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 77
// =============================================================
//
// QUESTION:
//   Grid: -1 wall, 0 gate, INF empty. Fill each empty with distance to nearest gate.
// =============================================================
const INF=2**31-1;
function walls(g){if(!g.length)return g;const m=g.length,n=g[0].length;const q=[];for(let i=0;i<m;i++)for(let j=0;j<n;j++)if(g[i][j]===0)q.push([i,j]);while(q.length){const [i,j]=q.shift();for(const [di,dj] of [[-1,0],[1,0],[0,-1],[0,1]]){const ni=i+di,nj=j+dj;if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]===INF){g[ni][nj]=g[i][j]+1;q.push([ni,nj]);}}}return g;}
const g=[[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]];
console.log(walls(g));
