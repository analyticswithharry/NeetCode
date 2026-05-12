// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 248 -- Detect Squares
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 124
// =============================================================
//
// QUESTION:
//   Add point or count axis-aligned squares with given query point.
// =============================================================
class DS{constructor(){this.c={};}_k(p){return p[0]+","+p[1];}add(p){const k=this._k(p);this.c[k]=(this.c[k]||0)+1;}count(p){const [x,y]=p;let tot=0;for(const k in this.c){const [a,b]=k.split(",").map(Number);if(a===x||Math.abs(a-x)!==Math.abs(b-y))continue;tot+=this.c[k]*(this.c[a+","+y]||0)*(this.c[x+","+b]||0);}return tot;}}
const d=new DS();[[3,10],[11,2],[3,2]].forEach(p=>d.add(p));console.log(d.count([11,10]));
