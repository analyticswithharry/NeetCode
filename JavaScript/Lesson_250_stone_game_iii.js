// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 250 -- Stone Game III
// Category   : 1-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 125
// =============================================================
//
// QUESTION:
//   Players take 1-3 stones from front; maximize own score. Return Alice/Bob/Tie.
// =============================================================
function stoneGameIII(s){const n=s.length;const dp=Array(n+1).fill(0);for(let i=n-1;i>=0;i--){let best=-Infinity,take=0;for(let k=0;k<3&&i+k<n;k++){take+=s[i+k];best=Math.max(best,take-dp[i+k+1]);}dp[i]=best;}return dp[0]>0?"Alice":dp[0]<0?"Bob":"Tie";}
console.log(stoneGameIII([1,2,3,7]));console.log(stoneGameIII([1,2,3,-9]));
