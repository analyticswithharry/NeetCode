// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 144 -- Decode Ways
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 72
// =============================================================
//
// QUESTION:
//   Number of ways to decode digit string s where '1'->A, ..., '26'->Z.
// =============================================================
function ways(s){if(!s||s[0]==='0')return 0;const n=s.length;const dp=new Array(n+1).fill(0);dp[0]=1;dp[1]=1;for(let i=2;i<=n;i++){if(s[i-1]!=='0')dp[i]+=dp[i-1];const x=+s.slice(i-2,i);if(x>=10&&x<=26)dp[i]+=dp[i-2];}return dp[n];}
console.log(ways("12"));console.log(ways("226"));console.log(ways("06"));
