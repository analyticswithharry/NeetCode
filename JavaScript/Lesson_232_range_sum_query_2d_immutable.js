// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 232 -- Range Sum Query 2D Immutable
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 116
// =============================================================
//
// QUESTION:
//   Build prefix sum 2D for O(1) region queries.
// =============================================================
class NM{constructor(m){const R=m.length,C=m[0].length;this.p=Array.from({length:R+1},()=>Array(C+1).fill(0));for(let i=0;i<R;i++)for(let j=0;j<C;j++)this.p[i+1][j+1]=m[i][j]+this.p[i][j+1]+this.p[i+1][j]-this.p[i][j];}sumRegion(r1,c1,r2,c2){return this.p[r2+1][c2+1]-this.p[r1][c2+1]-this.p[r2+1][c1]+this.p[r1][c1];}}
const n=new NM([[3,0,1],[5,6,3],[1,2,0]]);console.log(n.sumRegion(0,0,2,2));console.log(n.sumRegion(1,1,2,2));
