// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 136 -- Car Pooling
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 68
// =============================================================
//
// QUESTION:
//   Trips [numPassengers,from,to]; capacity. Return true iff possible to pick up & drop off all passengers without exceeding capacity.
// =============================================================
function carPool(t,cap){const e=new Array(1001).fill(0);for(const [n,a,b] of t){e[a]+=n;e[b]-=n;}let s=0;for(const v of e){s+=v;if(s>cap)return false;}return true;}
console.log(carPool([[2,1,5],[3,3,7]],4));console.log(carPool([[2,1,5],[3,3,7]],5));
