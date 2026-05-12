// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 124 -- Top K Frequent Elements
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 62
// =============================================================
//
// QUESTION:
//   Given an integer array nums and integer k, return the k most frequent elements.
// =============================================================
function topK(a,k){const m=new Map();for(const x of a)m.set(x,(m.get(x)||0)+1);return [...m.entries()].sort((p,q)=>q[1]-p[1]).slice(0,k).map(e=>e[0]);}
console.log(topK([1,1,1,2,2,3],2));
