// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 230 -- Integer Break
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 115
// =============================================================
//
// QUESTION:
//   Break n into >=2 positive ints; maximize product.
// =============================================================
function integerBreak(n){const dp=Array(n+1).fill(0);dp[1]=1;for(let i=2;i<=n;i++)for(let j=1;j<i;j++)dp[i]=Math.max(dp[i],j*Math.max(i-j,dp[i-j]));return dp[n];}
console.log(integerBreak(10));
