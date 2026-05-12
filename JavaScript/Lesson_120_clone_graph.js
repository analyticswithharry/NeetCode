// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 120 -- Clone Graph
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 60
// =============================================================
//
// QUESTION:
//   Given a node in a connected undirected graph, return a deep copy of the graph.
// =============================================================
class Node{constructor(v,n=[]){this.val=v;this.neighbors=n;}}
function clone(n){if(!n)return null;const seen=new Map();function dfs(x){if(seen.has(x))return seen.get(x);const c=new Node(x.val);seen.set(x,c);for(const y of x.neighbors)c.neighbors.push(dfs(y));return c;}return dfs(n);}
const a=new Node(1),b=new Node(2);a.neighbors=[b];b.neighbors=[a];const c=clone(a);console.log(c.val,c.neighbors[0].val,c.neighbors[0].neighbors[0].val);
