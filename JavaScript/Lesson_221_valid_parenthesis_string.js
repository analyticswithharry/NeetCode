// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 221 -- Valid Parenthesis String
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 111
// =============================================================
//
// QUESTION:
//   '*' can be '(' ')' or empty. Determine if string can be valid.
// =============================================================
function checkValid(s){let lo=0,hi=0;for(const c of s){lo+=c==='('?1:-1;hi+=c!==')'?1:-1;if(hi<0)return false;if(lo<0)lo=0;}return lo===0;}
console.log(checkValid("(*))"));console.log(checkValid("(*)"));
