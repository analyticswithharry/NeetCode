// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 115 -- Plus One
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 58
// =============================================================
//
// QUESTION:
//   Given a non-empty array of decimal digits representing a non-negative integer, add one and return the resulting array.
// =============================================================
function plusOne(d){d=d.slice();for(let i=d.length-1;i>=0;i--){if(d[i]<9){d[i]++;return d;}d[i]=0;}return [1,...d];}
console.log(plusOne([1,2,3]));console.log(plusOne([9,9]));
