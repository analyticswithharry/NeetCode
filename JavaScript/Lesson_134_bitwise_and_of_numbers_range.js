// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 134 -- Bitwise AND of Numbers Range
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 67
// =============================================================
//
// QUESTION:
//   Given range [m,n], return the bitwise AND of all numbers in this range, inclusive.
// =============================================================
function rangeAnd(m,n){let s=0;while(m!==n){m>>=1;n>>=1;s++;}return m<<s;}
console.log(rangeAnd(5,7));console.log(rangeAnd(0,0));
