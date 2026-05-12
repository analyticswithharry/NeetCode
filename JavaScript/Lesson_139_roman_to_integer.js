// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 139 -- Roman to Integer
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 70
// =============================================================
//
// QUESTION:
//   Convert Roman numeral string to integer.
// =============================================================
function r2i(s){const m={I:1,V:5,X:10,L:50,C:100,D:500,M:1000};let t=0,p=0;for(let i=s.length-1;i>=0;i--){const v=m[s[i]];if(v<p)t-=v;else{t+=v;p=v;}}return t;}
console.log(r2i("III"));console.log(r2i("LVIII"));console.log(r2i("MCMXCIV"));
