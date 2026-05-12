// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 147 -- Last Stone Weight II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 74
// =============================================================
//
// QUESTION:
//   Given stones, smash to minimize remaining weight (subset partition).
// =============================================================
function lsw2(s){const t=s.reduce((a,b)=>a+b,0),cap=Math.floor(t/2);const dp=new Array(cap+1).fill(false);dp[0]=true;for(const x of s)for(let j=cap;j>=x;j--)dp[j]=dp[j]||dp[j-x];for(let j=cap;j>=0;j--)if(dp[j])return t-2*j;}
console.log(lsw2([2,7,4,1,8,1]));console.log(lsw2([31,26,33,21,40]));
