// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 138 -- Matchsticks to Square
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 69
// =============================================================
//
// QUESTION:
//   Use all matchsticks to form a square. Return true if possible.
// =============================================================
function square(m){const s=m.reduce((a,b)=>a+b,0);if(s%4)return false;const side=s/4;m.sort((a,b)=>b-a);if(m[0]>side)return false;const sides=[0,0,0,0];function rec(i){if(i===m.length)return sides[0]===side&&sides[1]===side&&sides[2]===side;for(let j=0;j<4;j++){if(sides[j]+m[i]>side)continue;if(j>0&&sides[j]===sides[j-1])continue;sides[j]+=m[i];if(rec(i+1))return true;sides[j]-=m[i];}return false;}return rec(0);}
console.log(square([1,1,2,2,2]));console.log(square([3,3,3,3,4]));
