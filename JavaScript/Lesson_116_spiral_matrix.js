// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 116 -- Spiral Matrix
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 58
// =============================================================
//
// QUESTION:
//   Given m x n matrix, return all elements in spiral order.
// =============================================================
function spiral(m){const res=[];if(!m.length)return res;let t=0,b=m.length-1,l=0,r=m[0].length-1;while(t<=b&&l<=r){for(let j=l;j<=r;j++)res.push(m[t][j]);t++;for(let i=t;i<=b;i++)res.push(m[i][r]);r--;if(t<=b){for(let j=r;j>=l;j--)res.push(m[b][j]);b--;}if(l<=r){for(let i=b;i>=t;i--)res.push(m[i][l]);l++;}}return res;}
console.log(spiral([[1,2,3],[4,5,6],[7,8,9]]));
