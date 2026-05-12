// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 235 -- Product of Array Except Self
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 118
// =============================================================
//
// QUESTION:
//   Return array where output[i] = product of all nums except nums[i]. O(n) no division.
// =============================================================
function productExceptSelf(n){const o=Array(n.length).fill(1);let p=1;for(let i=0;i<n.length;i++){o[i]=p;p*=n[i];}p=1;for(let i=n.length-1;i>=0;i--){o[i]*=p;p*=n[i];}return o;}
console.log(productExceptSelf([1,2,3,4]));
