// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 143 -- Palindromic Substrings
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 72
// =============================================================
//
// QUESTION:
//   Count number of palindromic substrings in s.
// =============================================================
function count(s){let c=0;for(let i=0;i<s.length;i++){for(const [a0,b0] of [[i,i],[i,i+1]]){let a=a0,b=b0;while(a>=0&&b<s.length&&s[a]===s[b]){c++;a--;b++;}}}return c;}
console.log(count("abc"));console.log(count("aaa"));
