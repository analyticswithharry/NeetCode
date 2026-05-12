// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 131 -- Time Based Key Value Store
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 66
// =============================================================
//
// QUESTION:
//   Design TimeMap: set(k,v,t) and get(k,t) returns value with greatest timestamp <= t.
// =============================================================
class TimeMap{constructor(){this.m=new Map();}set(k,v,t){if(!this.m.has(k))this.m.set(k,[[],[]]);const [ts,vs]=this.m.get(k);ts.push(t);vs.push(v);}get(k,t){if(!this.m.has(k))return "";const [ts,vs]=this.m.get(k);let lo=0,hi=ts.length-1,r=-1;while(lo<=hi){const m=(lo+hi)>>1;if(ts[m]<=t){r=m;lo=m+1;}else hi=m-1;}return r<0?"":vs[r];}}
const tm=new TimeMap();tm.set("foo","bar",1);console.log(tm.get("foo",1));console.log(tm.get("foo",3));tm.set("foo","bar2",4);console.log(tm.get("foo",4));console.log(tm.get("foo",5));
