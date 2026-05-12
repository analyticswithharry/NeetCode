// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 114 -- Search In Rotated Sorted Array II
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 57
// =============================================================
//
// QUESTION:
//   Rotated sorted array may contain duplicates. Return true if target exists.
// =============================================================
function search(a,t){let lo=0,hi=a.length-1;while(lo<=hi){const m=(lo+hi)>>1;if(a[m]===t)return true;if(a[lo]===a[m]&&a[m]===a[hi]){lo++;hi--;}else if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return false;}
console.log(search([2,5,6,0,0,1,2],0));
console.log(search([2,5,6,0,0,1,2],3));
