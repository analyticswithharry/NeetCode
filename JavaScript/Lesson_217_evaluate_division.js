// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 217 -- Evaluate Division
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 109
// =============================================================
//
// QUESTION:
//   Given equations a/b=value, answer queries x/y. Build weighted graph and DFS.
// =============================================================
function calcEquation(eq,vals,q){const g={};const add=(a,b,v)=>{(g[a]=g[a]||{})[b]=v;};for(let i=0;i<eq.length;i++){add(eq[i][0],eq[i][1],vals[i]);add(eq[i][1],eq[i][0],1/vals[i]);}const dfs=(s,t,seen)=>{if(!(s in g)||!(t in g))return -1;if(s===t)return 1;seen.add(s);for(const n in g[s]){if(seen.has(n))continue;const r=dfs(n,t,seen);if(r!==-1)return g[s][n]*r;}return -1;};return q.map(([a,b])=>dfs(a,b,new Set()));}
console.log(calcEquation([["a","b"],["b","c"]],[2,3],[["a","c"],["b","a"],["a","e"]]));
