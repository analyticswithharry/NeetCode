// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 158 -- Minimum Array End
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 79
// =============================================================
//
// QUESTION:
//   Given n and x, return min possible value v such that AND of n distinct integers (>=x, <=v, all sharing bits of x) equals x. Equivalent: spread (n-1) over the zero-bits of x.
// =============================================================
function minEnd(n,x){n--;let r=BigInt(x),bit=1n,nb=1n,nn=BigInt(n),X=BigInt(x);while(nb<=nn){if((X&bit)===0n){if((nn&nb)!==0n)r|=bit;nb<<=1n;}bit<<=1n;}return r.toString();}
console.log(minEnd(3,4));console.log(minEnd(2,7));
