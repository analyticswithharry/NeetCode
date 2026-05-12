// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 223 -- Burst Balloons
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 112
// =============================================================
//
// QUESTION:
//   Burst balloons; coins = nums[l]*nums[i]*nums[r]. Maximize total.
// =============================================================
function maxCoins(nums){const a=[1,...nums,1],n=a.length;const dp=Array.from({length:n},()=>Array(n).fill(0));for(let L=2;L<n;L++)for(let l=0;l+L<n;l++){const r=l+L;for(let i=l+1;i<r;i++)dp[l][r]=Math.max(dp[l][r],dp[l][i]+dp[i][r]+a[l]*a[i]*a[r]);}return dp[0][n-1];}
console.log(maxCoins([3,1,5,8]));
