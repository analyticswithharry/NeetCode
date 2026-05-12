// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 066 -- Sort Colors
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 33
// =============================================================
//
// QUESTION:
//   Sort an array containing only 0,1,2 in-place. Dutch National Flag.
//
//   Example: [2,0,2,1,1,0] -> [0,0,1,1,2,2]
// =============================================================

var sortColors = function(nums){
    let l=0,m=0,r=nums.length-1;
    while (m<=r){
        if (nums[m]===0){ [nums[l],nums[m]]=[nums[m],nums[l]]; l++; m++; }
        else if (nums[m]===2){ [nums[m],nums[r]]=[nums[r],nums[m]]; r--; }
        else m++;
    }
    return nums;
};
console.log(sortColors([2,0,2,1,1,0]));
