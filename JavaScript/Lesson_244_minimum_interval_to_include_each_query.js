// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 244 -- Minimum Interval to Include Each Query
// Category   : Intervals
// Difficulty : Hard
// Study Plan : Day 122
// =============================================================
//
// QUESTION:
//   For each query q, find smallest interval covering q.
// =============================================================
function minInterval(iv,q){iv.sort((a,b)=>a[0]-b[0]);const sq=[...q].map((v,i)=>[v,i]).sort((a,b)=>a[0]-b[0]);const res=Array(q.length);const h=[];const push=x=>{h.push(x);h.sort((a,b)=>a[0]-b[0]);};let i=0;for(const [v,idx] of sq){while(i<iv.length&&iv[i][0]<=v){push([iv[i][1]-iv[i][0]+1,iv[i][1]]);i++;}while(h.length&&h[0][1]<v)h.shift();res[idx]=h.length?h[0][0]:-1;}return res;}
console.log(minInterval([[1,4],[2,4],[3,6],[4,4]],[2,3,4,5]));
