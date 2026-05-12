// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 065 -- Squares of a Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 33
// =============================================================
//
// QUESTION:
//   Given a sorted (non-decreasing) array, return an array of squares of each number, also sorted.
//
//   Example: [-4,-1,0,3,10] -> [0,1,9,16,100]
// =============================================================

var sortedSquares = function(nums){
    const n=nums.length, out=new Array(n); let l=0,r=n-1,k=n-1;
    while (l<=r){ if (Math.abs(nums[l])>Math.abs(nums[r])){ out[k]=nums[l]*nums[l]; l++; } else { out[k]=nums[r]*nums[r]; r--; } k--; }
    return out;
};
console.log(sortedSquares([-4,-1,0,3,10]));
