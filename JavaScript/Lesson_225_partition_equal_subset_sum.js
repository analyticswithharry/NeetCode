// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 225 -- Partition Equal Subset Sum
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 113
// =============================================================
//
// QUESTION:
//   Can the array be split into two equal-sum subsets? Subset-sum DP.
// =============================================================
function canPartition(nums){const s=nums.reduce((a,b)=>a+b,0);if(s&1)return false;const t=s/2;const dp=new Set([0]);for(const x of nums){const nd=new Set(dp);for(const v of dp)if(v+x<=t)nd.add(v+x);if(nd.has(t))return true;dp.clear();for(const v of nd)dp.add(v);}return dp.has(t);}
console.log(canPartition([1,5,11,5]));console.log(canPartition([1,2,3,5]));
