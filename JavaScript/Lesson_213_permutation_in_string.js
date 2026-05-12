// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 213 -- Permutation in String
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 107
// =============================================================
//
// QUESTION:
//   Return true if s2 contains a permutation of s1.
// =============================================================
function checkInclusion(s1,s2){if(s1.length>s2.length)return false;const a=Array(26).fill(0),b=Array(26).fill(0);for(const c of s1)a[c.charCodeAt(0)-97]++;for(let i=0;i<s2.length;i++){b[s2.charCodeAt(i)-97]++;if(i>=s1.length)b[s2.charCodeAt(i-s1.length)-97]--;if(a.every((v,j)=>v===b[j]))return true;}return false;}
console.log(checkInclusion("ab","eidbaooo"));console.log(checkInclusion("ab","eidboaoo"));
