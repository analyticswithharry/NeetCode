// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 211 -- Redundant Connection
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 106
// =============================================================
//
// QUESTION:
//   Given an n-node tree with one extra edge (forming exactly one cycle), return the edge that can be removed.
// =============================================================
function findRedundant(e){const p=Array.from({length:e.length+1},(_,i)=>i);const f=x=>{while(p[x]!==x){p[x]=p[p[x]];x=p[x];}return x;};for(const [a,b] of e){const ra=f(a),rb=f(b);if(ra===rb)return [a,b];p[ra]=rb;}}
console.log(findRedundant([[1,2],[1,3],[2,3]]));console.log(findRedundant([[1,2],[2,3],[3,4],[1,4],[1,5]]));
