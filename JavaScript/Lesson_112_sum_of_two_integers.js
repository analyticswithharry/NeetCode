// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 112 -- Sum of Two Integers
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 56
// =============================================================
//
// QUESTION:
//   Given two integers a and b, return the sum without using + or -.
// =============================================================
function add(a,b){while(b!==0){const c=(a&b)<<1;a=a^b;b=c;}return a|0;}
console.log(add(1,2));console.log(add(-2,3));
