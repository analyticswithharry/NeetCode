// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 231 -- Encode and Decode Strings
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 116
// =============================================================
//
// QUESTION:
//   Length-prefix encoding for arbitrary strings.
// =============================================================
function encode(a){return a.map(s=>s.length+"#"+s).join("");}
function decode(s){const r=[];let i=0;while(i<s.length){let j=s.indexOf('#',i);const n=+s.slice(i,j);r.push(s.slice(j+1,j+1+n));i=j+1+n;}return r;}
const e=encode(["hello","world","#42"]);console.log(e);console.log(decode(e));
