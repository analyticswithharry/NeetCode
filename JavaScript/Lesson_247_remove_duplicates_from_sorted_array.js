// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 247 -- Remove Duplicates From Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 124
// =============================================================
//
// QUESTION:
//   In-place dedupe of sorted array. Return new length.
// =============================================================
function dedupe(a){if(!a.length)return 0;let k=1;for(let i=1;i<a.length;i++)if(a[i]!==a[k-1])a[k++]=a[i];return k;}
const a=[1,1,2,2,3];const n=dedupe(a);console.log(n,a.slice(0,n));
