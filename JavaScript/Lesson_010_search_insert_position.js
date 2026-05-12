// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 010 -- Search Insert Position
// Category   : Binary Search
// Difficulty : Easy
// Study Plan : Day 5
// =============================================================
//
// QUESTION:
//   Given a sorted array of distinct integers and a target, return the
//   index if the target is found. If not, return the index where it would
//   be inserted in order. Must run in O(log n).
//
//   Example:
//     Input : nums = [1,3,5,6], target = 5    Output: 2
//     Input : nums = [1,3,5,6], target = 2    Output: 1
// =============================================================

var searchInsert = function(nums, target) {
    let l = 0, r = nums.length;
    while (l < r) {
        const m = (l + r) >> 1;
        if (nums[m] < target) l = m + 1; else r = m;
    }
    return l;
};

console.log(searchInsert([1,3,5,6], 5)); // 2
console.log(searchInsert([1,3,5,6], 2)); // 1
