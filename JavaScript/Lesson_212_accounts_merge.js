// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 212 -- Accounts Merge
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 106
// =============================================================
//
// QUESTION:
//   Merge accounts that share any common email. Return merged accounts with name + sorted unique emails.
// =============================================================
function accountsMerge(acc){const p={},own={};const f=x=>{while(p[x]!==x){p[x]=p[p[x]];x=p[x];}return x;};for(const a of acc){for(let i=1;i<a.length;i++){const e=a[i];if(!(e in p))p[e]=e;own[e]=a[0];p[f(e)]=f(a[1]);}}const g={};for(const e in p){const r=f(e);(g[r]=g[r]||[]).push(e);}return Object.values(g).map(v=>[own[v[0]],...v.sort()]);}
console.log(accountsMerge([["A","a@x","b@x"],["A","b@x","c@x"],["B","d@x"]]));
