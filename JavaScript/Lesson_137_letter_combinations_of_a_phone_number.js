// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 137 -- Letter Combinations of a Phone Number
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 69
// =============================================================
//
// QUESTION:
//   Given digits 2-9, return all possible letter combinations the number could represent.
// =============================================================
function letters(d){if(!d)return [];const m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'};let r=[''];for(const c of d){const n=[];for(const p of r)for(const x of m[c])n.push(p+x);r=n;}return r;}
console.log(letters("23"));
