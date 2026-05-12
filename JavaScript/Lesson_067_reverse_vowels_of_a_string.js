// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 067 -- Reverse Vowels of a String
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 34
// =============================================================
//
// QUESTION:
//   Reverse only the vowels of a string. Vowels: a,e,i,o,u (and uppercase).
//
//   Example: hello -> holle
// =============================================================

var reverseVowels = function(s){
    const v = new Set("aeiouAEIOU"); const a = s.split(""); let l=0,r=a.length-1;
    while (l<r){ while (l<r && !v.has(a[l])) l++; while (l<r && !v.has(a[r])) r--;
        [a[l],a[r]] = [a[r],a[l]]; l++; r--; }
    return a.join("");
};
console.log(reverseVowels("hello"), reverseVowels("leetcode"));
