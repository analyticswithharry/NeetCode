// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 224 -- Regular Expression Matching
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 112
// =============================================================
//
// QUESTION:
//   Implement regex with '.' and '*' (zero or more of preceding).
// =============================================================
function isMatch(s,p){const m=s.length,n=p.length;const dp=Array.from({length:m+1},()=>Array(n+1).fill(false));dp[0][0]=true;for(let j=1;j<=n;j++)if(p[j-1]==='*')dp[0][j]=dp[0][j-2];for(let i=1;i<=m;i++)for(let j=1;j<=n;j++){if(p[j-1]==='.'||p[j-1]===s[i-1])dp[i][j]=dp[i-1][j-1];else if(p[j-1]==='*')dp[i][j]=dp[i][j-2]||((p[j-2]==='.'||p[j-2]===s[i-1])&&dp[i-1][j]);}return dp[m][n];}
console.log(isMatch("aa","a*"));console.log(isMatch("ab",".*"));
