// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 155 -- Build a Matrix With Conditions
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 78
// =============================================================
//
// QUESTION:
//   Given k rows/cols and conditions for row/col orderings, place 1..k so each appears once and conditions are satisfied. Return matrix or [].
// =============================================================
function topo(k,conds){const adj=Array.from({length:k+1},()=>[]);const ind=new Array(k+1).fill(0);for(const [a,b] of conds){adj[a].push(b);ind[b]++;}const q=[];for(let i=1;i<=k;i++)if(ind[i]===0)q.push(i);const o=[];while(q.length){const x=q.shift();o.push(x);for(const y of adj[x]){if(--ind[y]===0)q.push(y);}}return o.length===k?o:[];}
function build(k,rC,cC){const r=topo(k,rC),c=topo(k,cC);if(!r.length||!c.length)return [];const pos={};c.forEach((v,i)=>pos[v]=i);const g=Array.from({length:k},()=>new Array(k).fill(0));r.forEach((v,i)=>g[i][pos[v]]=v);return g;}
console.log(build(3,[[1,2],[3,2]],[[2,1],[3,2]]));
