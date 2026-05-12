// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 215 -- Merge Triplets to Form Target Triplet
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 108
// =============================================================
//
// QUESTION:
//   Pick triplets where every value <= target; check if max across them equals target.
// =============================================================
function mergeTriplets(t,T){const g=[0,0,0];for(const x of t)if(x[0]<=T[0]&&x[1]<=T[1]&&x[2]<=T[2])for(let i=0;i<3;i++)g[i]=Math.max(g[i],x[i]);return g[0]===T[0]&&g[1]===T[1]&&g[2]===T[2];}
console.log(mergeTriplets([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]));
