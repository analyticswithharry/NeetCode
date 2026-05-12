// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 132 -- Split Array Largest Sum
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 66
// =============================================================
//
// QUESTION:
//   Split nums into k non-empty contiguous parts to minimize the largest sum among parts.
// =============================================================
function split(a,k){const can=mx=>{let c=1,s=0;for(const x of a){if(s+x>mx){c++;s=x;}else s+=x;}return c<=k;};let lo=Math.max(...a),hi=a.reduce((p,q)=>p+q,0);while(lo<hi){const m=(lo+hi)>>1;if(can(m))hi=m;else lo=m+1;}return lo;}
console.log(split([7,2,5,10,8],2));
