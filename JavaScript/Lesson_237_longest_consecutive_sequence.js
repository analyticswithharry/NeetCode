// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 237 -- Longest Consecutive Sequence
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 119
// =============================================================
//
// QUESTION:
//   Length of longest run of consecutive integers in unsorted array. O(n) hashset.
// =============================================================
function longestConsec(n){const s=new Set(n);let best=0;for(const x of s){if(!s.has(x-1)){let y=x;while(s.has(y+1))y++;best=Math.max(best,y-x+1);}}return best;}
console.log(longestConsec([100,4,200,1,3,2]));
