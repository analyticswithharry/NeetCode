// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 241 -- First Missing Positive
// Category   : Arrays and Hashing
// Difficulty : Hard
// Study Plan : Day 121
// =============================================================
//
// QUESTION:
//   Smallest missing positive int. O(n) time, O(1) extra space (cyclic placement).
// =============================================================
function firstMissing(n){const N=n.length;for(let i=0;i<N;i++)while(n[i]>=1&&n[i]<=N&&n[n[i]-1]!==n[i]){const j=n[i]-1;[n[i],n[j]]=[n[j],n[i]];}for(let i=0;i<N;i++)if(n[i]!==i+1)return i+1;return N+1;}
console.log(firstMissing([3,4,-1,1]));console.log(firstMissing([1,2,0]));
