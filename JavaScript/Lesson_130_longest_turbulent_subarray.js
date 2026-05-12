// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 130 -- Longest Turbulent Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 65
// =============================================================
//
// QUESTION:
//   Given an array, return length of longest turbulent subarray (alternating > <).
// =============================================================
function turb(a){let inc=1,dec=1,b=1;for(let i=1;i<a.length;i++){if(a[i]>a[i-1]){inc=dec+1;dec=1;}else if(a[i]<a[i-1]){dec=inc+1;inc=1;}else{inc=dec=1;}b=Math.max(b,inc,dec);}return b;}
console.log(turb([9,4,2,10,7,8,8,1,9]));
