// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 127 -- Number of 1 Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 64
// =============================================================
//
// QUESTION:
//   Return the number of 1 bits in unsigned int.
// =============================================================
function hw(n){let c=0;while(n){n&=n-1;c++;}return c;}
console.log(hw(11));console.log(hw(128));
