// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 002 -- Two Sum II Input Array Is Sorted
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 1
// =============================================================
//
// QUESTION:
//   Given a 1-indexed sorted array of integers `numbers`, find two numbers
//   such that they add up to a specific `target`. Return their 1-based
//   indices as [index1, index2]. Use O(1) extra space.
//
//   Example:
//     Input : numbers = [2,7,11,15], target = 9
//     Output: [1,2]   (because 2 + 7 = 9)
// =============================================================

var twoSum = function(numbers, target) {
    let l = 0, r = numbers.length - 1;
    while (l < r) {
        const s = numbers[l] + numbers[r];
        if (s === target) return [l+1, r+1];
        if (s < target) l++; else r--;
    }
    return [];
};

console.log(twoSum([2,7,11,15], 9)); // [1, 2]
