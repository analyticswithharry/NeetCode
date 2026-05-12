// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 128 -- Reverse Integer
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 64
// =============================================================
//
// QUESTION:
//   Reverse digits of a signed 32-bit integer; return 0 on overflow.
// =============================================================
function rev(x){const s=x<0?-1:1;x=Math.abs(x);let r=0;while(x){r=r*10+x%10;x=Math.floor(x/10);}r*=s;if(r<-2**31||r>2**31-1)return 0;return r;}
console.log(rev(123));console.log(rev(-456));console.log(rev(1534236469));
