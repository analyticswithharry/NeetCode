// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 238 -- Best Time to Buy And Sell Stock II
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 119
// =============================================================
//
// QUESTION:
//   Multiple transactions allowed. Sum positive deltas.
// =============================================================
function maxProfit(p){let s=0;for(let i=1;i<p.length;i++)s+=Math.max(0,p[i]-p[i-1]);return s;}
console.log(maxProfit([7,1,5,3,6,4]));
