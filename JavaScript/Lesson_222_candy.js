// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 222 -- Candy
// Category   : Greedy
// Difficulty : Hard
// Study Plan : Day 111
// =============================================================
//
// QUESTION:
//   Each child gets >=1 candy; higher rating gets more than neighbors. Return min candies.
// =============================================================
function candy(r){const n=r.length,a=Array(n).fill(1);for(let i=1;i<n;i++)if(r[i]>r[i-1])a[i]=a[i-1]+1;for(let i=n-2;i>=0;i--)if(r[i]>r[i+1])a[i]=Math.max(a[i],a[i+1]+1);return a.reduce((x,y)=>x+y);}
console.log(candy([1,0,2]));console.log(candy([1,2,2]));
