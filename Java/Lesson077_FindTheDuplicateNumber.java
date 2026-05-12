// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 077 -- Find the Duplicate Number
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 39
// =============================================================
//
// QUESTION:
//   An array of n+1 integers in [1,n] has exactly one duplicate. Find it (Floyd cycle detection, O(n) time, O(1) space).
// =============================================================

public class Lesson077_FindTheDuplicateNumber {
    public int findDuplicate(int[] nums){
        int slow = nums[0], fast = nums[0];
        do { slow = nums[slow]; fast = nums[nums[fast]]; } while (slow != fast);
        slow = nums[0];
        while (slow != fast){ slow = nums[slow]; fast = nums[fast]; }
        return slow;
    }
    public static void main(String[] a){
        System.out.println(new Lesson077_FindTheDuplicateNumber().findDuplicate(new int[]{1,3,4,2,2}));
        System.out.println(new Lesson077_FindTheDuplicateNumber().findDuplicate(new int[]{3,1,3,4,2}));
    }
}
