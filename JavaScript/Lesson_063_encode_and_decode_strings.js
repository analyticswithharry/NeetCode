// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 063 -- Encode and Decode Strings
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 32
// =============================================================
//
// QUESTION:
//   Design encode/decode of a list of strings into one string and back.
//
//   Strategy: prefix each string with its length and a delimiter (e.g., 5#hello).
// =============================================================

const encode = strs => strs.map(s => s.length + "#" + s).join("");
const decode = s => { const out=[]; let i=0;
    while (i < s.length){ const j=s.indexOf("#",i); const n=+s.slice(i,j);
        out.push(s.slice(j+1,j+1+n)); i = j+1+n; } return out; };
const e = encode(["lint","code","love","you"]); console.log(e); console.log(decode(e));
