// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 133 -- Counting Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 67
// =============================================================
//
// QUESTION:
//   For 0..n return array where ans[i] = number of 1-bits in i.
// =============================================================
function cb(n){const a=new Array(n+1).fill(0);for(let i=1;i<=n;i++)a[i]=a[i>>1]+(i&1);return a;}
console.log(cb(5));
