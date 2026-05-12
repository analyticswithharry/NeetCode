// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 240 -- Subarray Sum Equals K
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 120
// =============================================================
//
// QUESTION:
//   Count subarrays with sum k using prefix-sum frequency map.
// =============================================================
function subarraySum(n,k){let s=0,c=0;const m={0:1};for(const x of n){s+=x;c+=m[s-k]||0;m[s]=(m[s]||0)+1;}return c;}
console.log(subarraySum([1,1,1],2));console.log(subarraySum([1,2,3],3));
