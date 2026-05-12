// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 218 -- Minimum Height Trees
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 109
// =============================================================
//
// QUESTION:
//   Given an undirected tree, find roots that produce minimum-height trees (peel leaves BFS).
// =============================================================
function findMHT(n,e){if(n===1)return[0];const g=Array.from({length:n},()=>new Set()),d=Array(n).fill(0);for(const [a,b] of e){g[a].add(b);g[b].add(a);d[a]++;d[b]++;}let q=[];for(let i=0;i<n;i++)if(d[i]===1)q.push(i);let rem=n;while(rem>2){rem-=q.length;const nq=[];for(const x of q)for(const y of g[x]){d[y]--;if(d[y]===1)nq.push(y);}q=nq;}return q;}
console.log(findMHT(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]));
