// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 226 -- Combination Sum IV
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 113
// =============================================================
//
// QUESTION:
//   Count ordered combinations of nums summing to target.
// =============================================================
function combSum4(nums,t){const dp=Array(t+1).fill(0);dp[0]=1;for(let v=1;v<=t;v++)for(const x of nums)if(v>=x)dp[v]+=dp[v-x];return dp[t];}
console.log(combSum4([1,2,3],4));
