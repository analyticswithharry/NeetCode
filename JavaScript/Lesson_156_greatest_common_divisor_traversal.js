// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 156 -- Greatest Common Divisor Traversal
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 78
// =============================================================
//
// QUESTION:
//   You can move between indices i,j if gcd(nums[i],nums[j])>1. Return true iff every pair is connected.
// =============================================================
function primes(x){const r=[];let d=2;while(d*d<=x){if(x%d===0){r.push(d);while(x%d===0)x=Math.floor(x/d);}d++;}if(x>1)r.push(x);return r;}
function can(a){const n=a.length;const par=Array.from({length:n},(_,i)=>i);function f(x){while(par[x]!==x){par[x]=par[par[x]];x=par[x];}return x;}function u(x,y){x=f(x);y=f(y);if(x!==y)par[x]=y;}const pm=new Map();for(let i=0;i<n;i++)for(const p of primes(a[i])){if(pm.has(p))u(i,pm.get(p));else pm.set(p,i);}const r=f(0);for(let i=0;i<n;i++)if(f(i)!==r)return false;return true;}
console.log(can([2,3,6]));console.log(can([3,9,5]));console.log(can([4,3,12,8]));
