// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 009 -- Binary Search
// Category   : Binary Search
// Difficulty : Easy
// Study Plan : Day 5
// =============================================================
//
// QUESTION:
//   Given a sorted (ascending) array of integers nums and a target, return
//   the index of target if it exists, otherwise -1. You must run in O(log n).
//
//   Example:
//     Input : nums = [-1,0,3,5,9,12], target = 9
//     Output: 4
// =============================================================

public class Lesson009_BinarySearch {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = (l + r) >>> 1;
            if (nums[m] == target) return m;
            if (nums[m] < target) l = m + 1; else r = m - 1;
        }
        return -1;
    }
    public static void main(String[] args) {
        System.out.println(new Lesson009_BinarySearch().search(new int[]{-1,0,3,5,9,12}, 9));
    }
}
