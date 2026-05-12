// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 125 -- Merge Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 63
// =============================================================
//
// QUESTION:
//   Given nums1 (length m+n) and nums2 (length n) sorted, merge nums2 into nums1 in-place sorted.
// =============================================================
function merge(a,m,b,n){let i=m-1,j=n-1,k=m+n-1;while(j>=0){if(i>=0&&a[i]>b[j]){a[k--]=a[i--];}else{a[k--]=b[j--];}}return a;}
console.log(merge([1,2,3,0,0,0],3,[2,5,6],3));
