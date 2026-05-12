// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 008 -- Maximum Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 4
// =============================================================
//
// QUESTION:
//   Given an integer array nums, find the contiguous subarray (containing
//   at least one number) which has the largest sum and return its sum.
//
//   Example:
//     Input : nums = [-2,1,-3,4,-1,2,1,-5,4]
//     Output: 6   (subarray [4,-1,2,1])
// =============================================================

public class Lesson008_MaximumSubarray {
    public int maxSubArray(int[] nums) {
        int best = nums[0], cur = nums[0];
        for (int i = 1; i < nums.length; i++) {
            cur = Math.max(nums[i], cur + nums[i]);
            best = Math.max(best, cur);
        }
        return best;
    }
    public static void main(String[] args) {
        System.out.println(new Lesson008_MaximumSubarray().maxSubArray(new int[]{-2,1,-3,4,-1,2,1,-5,4}));
    }
}
