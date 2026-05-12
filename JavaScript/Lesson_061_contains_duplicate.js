// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 061 -- Contains Duplicate
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 31
// =============================================================
//
// QUESTION:
//   Given an integer array nums, return true if any value appears at least twice.
//
//   Example: [1,2,3,1] -> true; [1,2,3,4] -> false
// =============================================================

var containsDuplicate = function(nums){ return new Set(nums).size !== nums.length; };
console.log(containsDuplicate([1,2,3,1]), containsDuplicate([1,2,3,4]));
