// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 157 -- Add Binary
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 79
// =============================================================
//
// QUESTION:
//   Given two binary strings, return their sum as a binary string.
// =============================================================
function addBin(a,b){let i=a.length-1,j=b.length-1,c=0;const r=[];while(i>=0||j>=0||c){const s=c+(i>=0?+a[i--]:0)+(j>=0?+b[j--]:0);r.push(s%2);c=s>>1;}return r.reverse().join("");}
console.log(addBin("11","1"));console.log(addBin("1010","1011"));
