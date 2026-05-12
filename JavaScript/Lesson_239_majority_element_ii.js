// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 239 -- Majority Element II
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 120
// =============================================================
//
// QUESTION:
//   All elements appearing more than n/3 times. Boyer-Moore variant.
// =============================================================
function majorityIII(nums){let c1=0,c2=0,n1=null,n2=null;for(const x of nums){if(x===n1)c1++;else if(x===n2)c2++;else if(c1===0){n1=x;c1=1;}else if(c2===0){n2=x;c2=1;}else{c1--;c2--;}}return [...new Set([n1,n2])].filter(n=>n!==null&&nums.filter(y=>y===n).length>nums.length/3);}
console.log(majorityIII([3,2,3]));console.log(majorityIII([1,1,1,3,3,2,2,2]));
