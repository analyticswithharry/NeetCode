// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 129 -- Maximum Sum Circular Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 65
// =============================================================
//
// QUESTION:
//   Given a circular integer array, find the maximum subarray sum (subarray may wrap).
// =============================================================
function maxCirc(a){let tot=0,mxc=a[0],cur=a[0],mnc=a[0],cur2=a[0];for(let i=0;i<a.length;i++){if(i){cur=Math.max(a[i],cur+a[i]);mxc=Math.max(mxc,cur);cur2=Math.min(a[i],cur2+a[i]);mnc=Math.min(mnc,cur2);}tot+=a[i];}return mxc<0?mxc:Math.max(mxc,tot-mnc);}
console.log(maxCirc([1,-2,3,-2]));console.log(maxCirc([5,-3,5]));console.log(maxCirc([-3,-2,-3]));
